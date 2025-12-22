# Phase 5: Evaluation Report

**Date:** 2025-12-20  
**Project:** Clinic Legacy App  
**Team:** Nbee_Nt5rj.py

This document compares the codebase metrics before and after refactoring to demonstrate maintainability improvements.

---

## 1. Lines of Code (LOC) Comparison

### Before Refactoring
| File | Lines |
|------|-------|
| `app.py` | 128 |
| **Python Total** | **128** |
| `index.html` | 20 |
| `patients.html` | 15 |
| `patient_add.html` | 9 |
| `patient_edit.html` | 9 |
| `appointments.html` | 9 |
| `appointment_create.html` | 9 |
| **HTML Total** | **71** |
| **Grand Total** | **199** |

### After Refactoring
| File | Lines | Change |
|------|-------|--------|
| `app.py` | 164 | +36 (routes only, cleaner) |
| `models.py` | 46 | **NEW** |
| `repository.py` | 144 | **NEW** |
| **Python Total** | **354** | +226 |
| `index.html` | 20 | 0 |
| `patients.html` | 83 | +68 (flash messages, styling) |
| `patient_add.html` | 73 | +64 (validation, styling) |
| `patient_edit.html` | 73 | +64 (validation, styling) |
| `appointments.html` | 63 | +54 (search form, styling) |
| `appointment_create.html` | 80 | +71 (validation, styling) |
| **HTML Total** | **392** | +321 |
| **Grand Total** | **746** | +547 |

### LOC Analysis
- **Python LOC increased** due to:
  - Proper separation of concerns (3 files instead of 1)
  - Added docstrings and comments
  - New search functionality
  - Comprehensive validation logic
  
- **HTML LOC increased** due to:
  - Flash message templates
  - CSS styling (inline)
  - Search forms
  - HTML5 validation attributes

> **Note:** While LOC increased, the code is now **modular**, **maintainable**, and **testable**. Each file has a single responsibility.

---

## 2. Function Point Analysis (After Refactoring)

### Step 1: Unadjusted Function Points (UFP)

| Function Type | Count | Complexity | Weight | Total | Description |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **External Inputs (EI)** | 4 | Average | 4 | **16** | Add Patient, Edit Patient, Add Appointment, **Search** |
| **External Outputs (EO)** | 2 | Average | 5 | **10** | API: `/api/patients`, `/api/appointments` |
| **External Inquiries (EQ)** | 4 | Average | 4 | **16** | Index, Patient List, Appointment List, **Search Results** |
| **Internal Logical Files (ILF)** | 2 | Average | 10 | **20** | Repository: `_patients`, `_appointments` |
| **External Interface Files (EIF)**| 0 | Low | 7 | **0** | No external systems |
| **Total UFP** | | | | **62** | *(was 54)* |

### Step 2: Complexity Factor Adjustment (CFA)

| # | General System Characteristic | Before | After |
|---|------------------------------|--------|-------|
| 1 | Data communications | 0 | 0 |
| 2 | Distributed data processing | 0 | 0 |
| 3 | Performance | 0 | 0 |
| 4 | Heavily used configuration | 0 | 0 |
| 5 | Transaction rate | 0 | 0 |
| 6 | Online data entry | 4 | 4 |
| 7 | End-user efficiency | 3 | **4** *(search feature)* |
| 8 | Online update | 4 | 4 |
| 9 | Complex processing | 0 | **1** *(validation)* |
| 10 | Reusability | 0 | **3** *(modular design)* |
| 11 | Installation ease | 0 | 0 |
| 12 | Operational ease | 2 | **3** *(flash messages)* |
| 13 | Multiple sites | 0 | 0 |
| 14 | Facilitate change | 2 | **4** *(separated concerns)* |
| **Total Degree of Influence (TDI)** | **15** | **23** |

**CFA Calculation:**
- Formula: CFA = 0.65 + (0.01 × TDI)
- Before: 0.65 + (0.01 × 15) = **0.80**
- After: 0.65 + (0.01 × 23) = **0.88**

### Step 3: Adjusted Function Points (AFP)

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| UFP | 54 | 62 | +8 (+15%) |
| CFA | 0.80 | 0.88 | +0.08 |
| **AFP** | **43.2** | **54.6** | **+11.4 (+26%)** |

> The increase in AFP reflects added functionality (search, validation) and improved system characteristics.

---

## 3. COCOMO Estimation (After)

**Formulas (Organic Mode):**
- Effort (E) = 2.4 × (KLOC)^1.05
- Time (T) = 2.5 × (Effort)^0.38

### Calculations

| Metric | Before | After |
|--------|--------|-------|
| Python KLOC | 0.128 | 0.354 |
| Effort (PM) | 0.28 | 0.81 |
| Time (Months) | 1.5 | 2.1 |

**After Calculation:**
- E = 2.4 × (0.354)^1.05 = **0.81 Person-Months**
- T = 2.5 × (0.81)^0.38 = **2.1 Months**

> The increased effort reflects the added features and better architecture. However, **future maintenance** will require **less effort** due to improved modularity.

---

## 4. Qualitative Complexity Analysis

### Code Quality Metrics

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| **Coupling** | High (global state) | Low (repository pattern) | ✅ Much Better |
| **Cohesion** | Low (God Object) | High (SRP per file) | ✅ Much Better |
| **Duplicate Code** | 4 duplicate functions | 0 duplicates | ✅ 100% Eliminated |
| **Data Normalization** | Denormalized | Normalized | ✅ Fixed |
| **Input Validation** | None | Full validation | ✅ Added |
| **Error Handling** | Basic (400/404) | Flash messages | ✅ Improved |
| **Testability** | Poor | Good | ✅ Much Better |
| **Documentation** | None | Docstrings + comments | ✅ Added |

### Maintainability Index (Qualitative)

| Aspect | Before | After |
|--------|--------|-------|
| **Understandability** | 2/5 | 4/5 |
| **Modifiability** | 1/5 | 4/5 |
| **Testability** | 1/5 | 4/5 |
| **Reusability** | 1/5 | 4/5 |
| **Overall** | **1.25/5** | **4/5** |

---

## 5. Architecture Comparison

### Before: Monolithic Structure
```
app.py (128 lines)
├── Global state (patients, appointments, _next_id)
├── Helper functions (duplicated)
├── All routes
├── API endpoints
└── Seed data
```

### After: Modular Structure
```
project/
├── app.py (164 lines)         # Routes only
├── models.py (46 lines)       # Domain classes
├── repository.py (144 lines)  # Data management
└── templates/                  # Enhanced UI
    ├── index.html
    ├── patients.html          # +flash messages
    ├── patient_add.html       # +validation
    ├── patient_edit.html      # +validation
    ├── appointments.html      # +search
    └── appointment_create.html # +validation
```

---

## 6. Code Smells: Before vs After

| Code Smell | Before | After | Status |
|------------|--------|-------|--------|
| Duplicate Code | `add_patient_record` ≡ `create_patient`, `find_patient` ≡ `get_patient_by_id` | Consolidated to single functions | ✅ Fixed |
| Primitive Obsession | Patients/Appointments as dicts | `Patient` and `Appointment` classes | ✅ Fixed |
| God Object | `app.py` does everything | Split into 3 focused modules | ✅ Fixed |
| Feature Envy | Routes access global lists directly | Routes use `clinic` repository | ✅ Fixed |
| Shotgun Surgery | Appointments store full patient objects | Appointments store `patient_id` only | ✅ Fixed |
| Long Method | `del_patient` with manual filtering | `clinic.delete_patient()` method | ✅ Fixed |
| Missing Validation | No input validation | Full validation with flash messages | ✅ Fixed |

---

## 7. Screenshots

### Appointment Search Feature
The new search functionality allows filtering by patient name and/or date:
- URL: `/appointments?q=ahmed&date=2025-10-22`
- Case-insensitive name matching
- Exact date matching

### Form Validation
Error messages appear when submitting invalid forms:
- Required field validation
- Age range validation (0-150)
- Success/error flash messages with color coding

---

## 8. Unit Testing (Extra Credit)

One of the key benefits of the refactoring is improved **testability**. The original monolithic `app.py` with global state was nearly impossible to unit test. After extracting the `ClinicRepository` class, we can now test all data operations independently.

### Test File: `test_repository.py`

We created 17 unit tests covering 8+ functions using **pytest**.

### Test Command
```bash
python -m pytest test_repository.py -v
```

### Test Results
```
============================================= test session starts ==============================================
platform win32 -- Python 3.12.6, pytest-9.0.2
collected 17 items

test_repository.py::TestPatientOperations::test_add_patient_creates_patient_with_correct_data PASSED      [  5%]
test_repository.py::TestPatientOperations::test_add_patient_increments_id PASSED                          [ 11%]
test_repository.py::TestPatientOperations::test_find_patient_returns_correct_patient PASSED               [ 17%]
test_repository.py::TestPatientOperations::test_find_patient_returns_none_for_invalid_id PASSED           [ 23%]
test_repository.py::TestPatientOperations::test_get_all_patients_returns_all PASSED                       [ 29%]
test_repository.py::TestPatientOperations::test_update_patient_modifies_data PASSED                       [ 35%]
test_repository.py::TestPatientOperations::test_delete_patient_removes_patient PASSED                     [ 41%]
test_repository.py::TestAppointmentOperations::test_add_appointment_creates_appointment PASSED            [ 47%]
test_repository.py::TestAppointmentOperations::test_get_all_appointments_returns_all PASSED               [ 52%]
test_repository.py::TestAppointmentOperations::test_get_appointments_with_patient_names_enriches_data PASSED [ 58%]
test_repository.py::TestAppointmentOperations::test_search_appointments_filters_by_date PASSED            [ 64%]
test_repository.py::TestAppointmentOperations::test_search_appointments_filters_by_name PASSED            [ 70%]
test_repository.py::TestAppointmentOperations::test_search_appointments_is_case_insensitive PASSED        [ 76%]
test_repository.py::TestAppointmentOperations::test_delete_patient_removes_appointments PASSED            [ 82%]
test_repository.py::TestEdgeCases::test_update_nonexistent_patient_returns_none PASSED                    [ 88%]
test_repository.py::TestEdgeCases::test_empty_repository_returns_empty_lists PASSED                       [ 94%]
test_repository.py::TestEdgeCases::test_search_with_no_matches_returns_empty PASSED                       [100%]

============================================== 17 passed in 0.04s ==============================================
```

### Functions Tested

| # | Function | Tests |
|---|----------|-------|
| 1 | `add_patient()` | 2 tests |
| 2 | `find_patient()` | 2 tests |
| 3 | `get_all_patients()` | 1 test |
| 4 | `update_patient()` | 2 tests |
| 5 | `delete_patient()` | 2 tests (including cascade) |
| 6 | `add_appointment()` | 1 test |
| 7 | `get_all_appointments()` | 1 test |
| 8 | `get_appointments_with_patient_names()` | 1 test |
| 9 | `search_appointments()` | 4 tests |
| **Total** | **9 functions** | **17 tests** |

### Testability Improvement

| Aspect | Before | After |
|--------|--------|-------|
| Unit testable | ❌ No (global state) | ✅ Yes (isolated classes) |
| Test coverage | 0% | ~90% of repository |
| Test isolation | ❌ Impossible | ✅ Fresh instance per test |
| Mocking | ❌ Difficult | ✅ Easy (dependency injection) |

---

## 9. Conclusion

### Summary of Improvements

| Category | Before | After |
|----------|--------|-------|
| **Files** | 1 Python file | 3 Python files (modular) |
| **Architecture** | Monolithic | Layered (Routes → Repository → Models) |
| **Code Smells** | 6+ identified | 0 remaining |
| **Features** | Basic CRUD | CRUD + Search + Validation |
| **User Feedback** | None | Flash messages |
| **Maintainability** | Poor | Good |

### Trade-offs
- **LOC increased** from 199 to 746 (+275%)
- However, the code is now:
  - Easier to understand (single responsibility)
  - Easier to modify (low coupling)
  - Easier to test (dependency injection ready)
  - Better documented (docstrings)

### Recommendations for Future Work
1. ~~Add unit tests using pytest~~ ✅ **Done! (17 tests)**
2. Move to SQLite/PostgreSQL for persistent storage
3. Add user authentication
4. Create a proper CSS file instead of inline styles

---

**Evaluation Complete**  
*The refactoring successfully improved maintainability while preserving all original functionality and adding new features.*
