# Phase 2: Metrics & Estimation

**Date:** 2025-12-06
**Project:** Clinic Legacy App
**Team:** Nbee_Nt5rj.py

## 1. Lines of Code (LOC)
Using manual counting and `wc -l` validation on the current codebase:

* **Python (`app.py`):** 128 lines
* **HTML Templates (approx):** ~71 lines (across 6 template files)
* **Total Source Lines of Code (SLOC):** ~199 lines

## 2. Function Point Analysis (Detailed)

### Step 1: Calculate Unadjusted Function Points (UFP)
We identified the transaction functions and data entities in `app.py`.

| Function Type | Count | Complexity | Weight | Total | Description |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **External Inputs (EI)** | 3 | Average | 4 | **12** | Forms: Add Patient, Edit Patient, Add Appointment |
| **External Outputs (EO)** | 2 | Average | 5 | **10** | API Responses: `/api/patients`, `/api/appointments` |
| **External Inquiries (EQ)** | 3 | Average | 4 | **12** | Views: Index, Patient List, Appointment List |
| **Internal Logical Files (ILF)** | 2 | Average | 10 | **20** | Global Lists: `patients`, `appointments` |
| **External Interface Files (EIF)**| 0 | Low | 7 | **0** | No external systems |
| **Total UFP** | | | | **54** | |

### Step 2: Calculate Complexity Factor Adjustment (CFA)
We rated the 14 General System Characteristics (GSC) on a scale of 0 (None) to 5 (High). Most complexity factors are low.

1.  Data communications: **0**
2.  Distributed data processing: **0**
3.  Performance: **0**
4.  Heavily used configuration: **0**
5.  Transaction rate: **0**
6.  Online data entry: **4** (Core feature)
7.  End-user efficiency: **3** (Standard web forms)
8.  Online update: **4** (Real-time list updates)
9.  Complex processing: **0**
10. Reusability: **0**
11. Installation ease: **0**
12. Operational ease: **2**
13. Multiple sites: **0**
14. Facilitate change: **2**

**Total Degree of Influence (TDI):** 15

**CFA Calculation:**
* Formula: CFA = 0.65 + (0.01 * TDI)
* Calculation: 0.65 + (0.01 * 15) = 0.65 + 0.15
* **CFA = 0.80**

### Step 3: Calculate Adjusted Function Points (AFP)
* Formula: AFP = UFP * CFA
* Calculation: 54 * 0.80
* **AFP = 43.2 Function Points**

---

## 3. COCOMO Estimation
We used the **Basic COCOMO** model for an "Organic" project (small team, simple environment).

**Formulas:**
* Effort (E) = a * (KLOC)^b
* Time (T) = c * (Effort)^d

**Constants (Organic Mode):**
* a = 2.4
* b = 1.05
* c = 2.5
* d = 0.38

**Calculations:**

1.  **KLOC (Thousands of Lines):**
    0.128 KLOC (Based on 128 lines of Python)

2.  **Effort (Person-Months):**
    E = 2.4 * (0.128)^1.05
    E ≈ 0.28 Person-Months
    *(Roughly 1 week of effort)*

3.  **Development Time (Months):**
    T = 2.5 * (0.28)^0.38
    T ≈ 1.5 Months

**Interpretation:**
The COCOMO model estimates **1.5 months** for the full software lifecycle (including analysis, design, testing, and documentation), which aligns with the project's 5-week schedule.
