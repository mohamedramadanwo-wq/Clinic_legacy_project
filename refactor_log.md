# Refactoring Log

**Project:** Clinic Legacy App  
**Team:** Nbee_Nt5rj.py  
**Started:** 2025-12-22

This document records the before/after snapshots of each refactoring step.

---

## Phase 1: Create Model Classes (Sprint 1 - T-1.1)

**Date:** 2025-12-22  
**Commit:** `feat: Create Patient and Appointment model classes`  
**Code Smell Fixed:** Primitive Obsession

### Problem
Patients and Appointments were stored as plain dictionaries throughout the codebase:
```python
# Before: Using dictionaries
patient = {'id': 1, 'name': 'Ahmed', 'age': '30', 'phone': '091-111-222', 'notes': ''}
appointment = {'id': 1, 'patient': patient, 'date': '2025-10-22', 'description': 'Checkup'}
```

This approach has several issues:
- No type safety or validation
- Easy to misspell keys
- No encapsulation of behavior
- Difficult to add methods

### Solution
Created proper domain model classes in `models.py`:

```python
# After: Using classes
class Patient:
    def __init__(self, id, name, age, phone, notes=''):
        self.id = id
        self.name = name
        self.age = age
        self.phone = phone
        self.notes = notes
    
    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'age': self.age, 
                'phone': self.phone, 'notes': self.notes}

class Appointment:
    def __init__(self, id, patient_id, date, description):
        self.id = id
        self.patient_id = patient_id  # Normalized - stores ID only
        self.date = date
        self.description = description
```

### Files Changed
| File | Change |
|------|--------|
| `models.py` | **NEW** - Created with Patient and Appointment classes |

### Benefits
- Type safety through class attributes
- Encapsulated `to_dict()` method for serialization
- Foundation for adding validation and business logic
- Better IDE autocompletion and error detection

---

## Phase 2: Remove Duplicate Functions (Sprint 1 - T-1.2)

**Date:** 2025-12-22  
**Commit:** `refactor: Consolidate duplicate patient functions`  
**Code Smell Fixed:** Duplicate Code

### Problem
The codebase contained two pairs of identical functions:

```python
# DUPLICATE PAIR 1: Creating patients
def add_patient_record(name, age, phone):    # Used in patient_add route
    ...
def create_patient(name, age, phone):        # Unused duplicate
    ...

# DUPLICATE PAIR 2: Finding patients  
def find_patient(p_id):                      # Used in appointment_create
    ...
def get_patient_by_id(pid):                  # Used in patient_edit
    ...
```

### Solution
Consolidated to single, well-documented functions:

```python
def add_patient(name, age, phone):
    """Add a new patient to the system. (Consolidated)"""
    global _next_id
    patient = {'id': _next_id, 'name': name, 'age': age, 'phone': phone, 'notes': ''}
    patients.append(patient)
    _next_id += 1
    return patient

def find_patient(patient_id):
    """Find a patient by ID. (Consolidated)"""
    for p in patients:
        if p['id'] == patient_id:
            return p
    return None
```

### Files Changed
| File | Change |
|------|--------|
| `app.py` | Removed `create_patient()` and `get_patient_by_id()`, updated all references |

### LOC Impact
- **Before:** 26 lines (4 functions)
- **After:** 14 lines (2 functions)
- **Reduction:** 12 lines (-46%)

---

## Phase 3: Create Repository Class (Sprint 1 - T-1.3)

**Date:** 2025-12-22  
**Commit:** `refactor: Extract ClinicRepository from app.py`  
**Code Smell Fixed:** God Object / Low Cohesion / Feature Envy

### Problem
`app.py` was a monolithic "God Object" handling everything:
- Web routing
- Data storage (global lists)
- Data manipulation logic
- API endpoints

```python
# Before: Global state in app.py
patients = []
appointments = []
_next_id = 1

def add_patient(name, age, phone):
    global _next_id
    patient = {...}
    patients.append(patient)
    ...

def del_patient(pid):
    global patients, appointments
    # Manual filtering logic mixed with route
    newp = []
    for p in patients:
        if p['id'] != pid:
            newp.append(p)
    patients = newp
    ...
```

### Solution
Created `repository.py` with `ClinicRepository` class:

```python
# After: Clean separation of concerns
class ClinicRepository:
    def __init__(self):
        self._patients = []
        self._appointments = []
        self._next_patient_id = 1
    
    def add_patient(self, name, age, phone):
        """Add a new patient and return the patient dict."""
        patient = {...}
        self._patients.append(patient)
        return patient
    
    def delete_patient(self, patient_id):
        """Delete a patient and their appointments (cascade)."""
        self._patients = [p for p in self._patients if p['id'] != patient_id]
        self._appointments = [a for a in self._appointments if a['patient']['id'] != patient_id]

# Global instance
clinic = ClinicRepository()
```

Updated `app.py` to use repository:
```python
from repository import clinic

@app.route('/del_patient/<int:pid>')
def del_patient(pid):
    clinic.delete_patient(pid)  # Clean, single-responsibility
    return redirect(url_for('list_patients'))
```

### Files Changed
| File | Change |
|------|--------|
| `repository.py` | **NEW** - ClinicRepository class with all data operations |
| `app.py` | Removed global state, imports and uses `clinic` from repository |

### LOC Impact
- **app.py Before:** 121 lines
- **app.py After:** 107 lines
- **repository.py:** 101 lines (new, but encapsulated)
- **Total:** Better organized, each file has single responsibility

### Benefits
- **Single Responsibility:** Routes in `app.py`, data in `repository.py`
- **Testability:** Can unit test `ClinicRepository` independently
- **Encapsulation:** Data access controlled through methods
- **Maintainability:** Changes to data storage only affect `repository.py`

---

## Phase 4: Normalize Appointments (Sprint 2 - T-2.1)

**Date:** 2025-12-22  
**Commit:** `refactor: Normalize appointments to use patient_id`  
**Code Smell Fixed:** Shotgun Surgery / Tight Data Coupling

### Problem
Appointments stored a **copy** of the entire patient object:

```python
# Before: Storing full patient object
appointment = {
    'id': 1,
    'patient': {'id': 1, 'name': 'Ahmed', 'age': '30', 'phone': '091-111-222'},
    'date': '2025-10-22',
    'description': 'Checkup'
}
```

**Issues:**
- If patient name is updated, the appointment still shows old name
- Data duplication (patient data stored in multiple places)
- Deleting patients requires checking `a['patient']['id']` (fragile)

### Solution
Store only `patient_id` and look up patient details when needed:

```python
# After: Storing only patient_id (normalized)
appointment = {
    'id': 1,
    'patient_id': 1,  # Reference only
    'date': '2025-10-22',
    'description': 'Checkup'
}

# New helper method enriches data for display
def get_appointments_with_patient_names(self):
    enriched = []
    for a in self._appointments:
        patient = self.find_patient(a['patient_id'])
        enriched.append({
            'id': a['id'],
            'patient_id': a['patient_id'],
            'patient_name': patient['name'] if patient else 'Unknown',
            'date': a['date'],
            'description': a['description']
        })
    return enriched
```

### Files Changed
| File | Change |
|------|--------|
| `repository.py` | Changed `add_appointment()` to use `patient_id`, added `get_appointments_with_patient_names()` |
| `app.py` | Updated routes to pass `patient_id` and use enriched appointment data |
| `templates/index.html` | Changed `{{a.patient.name}}` to `{{a.patient_name}}` |
| `templates/appointments.html` | Changed `{{a.patient.name}}` to `{{a.patient_name}}` |

### Benefits
- **Data Consistency:** Patient updates automatically reflect in appointments
- **Reduced Coupling:** Appointments only depend on patient ID
- **Simpler Deletion:** Can filter by `a['patient_id'] != patient_id`
- **Single Source of Truth:** Patient data lives only in patients list

---
