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
