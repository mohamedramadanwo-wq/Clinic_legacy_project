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

