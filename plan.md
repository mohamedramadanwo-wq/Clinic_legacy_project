# Phase 3: Maintenance Plan & Schedule

**Date:** 2025-12-06
**Project:** Clinic Legacy App
**Team:** Nbee_Nt5rj.py

## 1. Backlog (User Stories)

We have identified the following maintenance tasks and evolution requirements, formatted as User Stories.

### Refactoring Stories (Technical Debt)
* **US-01:** As a developer, I want to create a `Patient` class so that patient data is validated and typed (removing primitive obsession).
* **US-02:** As a developer, I want to create a `ClinicRepository` class to manage global lists so that data persistence is decoupled from the web routes.
* **US-03:** As a developer, I want to remove duplicate code in `create_patient` and `add_patient_record` so that bug fixes only need to happen in one place.
* **US-04:** As a developer, I want to refactor appointments to store `patient_id` instead of the full patient object to prevent data inconsistency.

### Evolution Stories (New Features)
* **US-05:** As a user, I want to search for appointments by date or patient name so I can find records quickly. (Evolution Choice: *Improve Appointment Search*)
* **US-06:** As a user, I want to see error messages when I submit empty forms so that I don't create invalid records.

---

## 2. Sprint Plan

We have divided the work into two 1-week sprints based on the team's capacity.

### Sprint 1: Refactoring Core & Stability
**Goal:** Fix the "God Object" and "Duplicate Code" smells to stabilize the codebase before adding features.

| Task ID | Description | Assigned To |
| :--- | :--- | :--- | 
| **T-1.1** | Create `Patient` and `Appointment` classes to fix Primitive Obsession (US-01). | **Ali Agela** |
| **T-1.2** | Consolidate duplicate creation/search functions in `app.py` (US-03). | **Ali Agela** |
| **T-1.3** | Create `ClinicRepository` and move global lists there (US-02). | **Mohamed Ramadan** |
| **T-1.4** | Setup Trello Board and define Acceptance Criteria for all tasks. | **Mohamed Jamal** |

### Sprint 2: Data Integrity & Evolution Features
**Goal:** Fix data coupling (Shotgun Surgery) and implement the required evolution feature.

| Task ID | Description | Assigned To |
| :--- | :--- | :--- |
| **T-2.1** | Normalize Appointments: Switch from storing objects to `patient_id` (US-04). | **Ali Agela** |
| **T-2.2** | Implement "Appointment Search" feature and Unit Tests (US-05). | **Ali Agela** | 
| **T-2.3** | Implement Form Validation & Flash Messages (US-06). | **Mohamed Ramadan** | 
| **T-2.4** | Final Report compilation (`final_doc.md`) and presentation slides. | **Mohamed Ramadan** | 
| **T-2.5** | Final Project Coordination and deliverable review. | **Mohamed Jamal** |

---

## 3. Team Roles & Responsibilities

| Member | Role | Responsibilities |
| :--- | :--- | :--- |
| **Mohamed Jamal Al Tarhoni** | **Scrum Master** | Responsible for the Trello board management, tracking progress, coordinating the `Plan.md`, and ensuring team deliverables are met on time. |
| **Mohamed Ramadan Alwerfalli** | **Documentation Lead & Dev** | Responsible for the architectural analysis (`analysis.md`), metrics calculation (`metrics.md`), evaluation overview (`evaluation.md`), and the final presentation. Also assists with core refactoring. |
| **Ali Agela** | **Lead Developer** | Responsible for the heavy lifting of code refactoring (Classes, Repository), implementing the Evolution Features (Search, handling error messages), and writing Unit Tests. |

---

## 4. Risk Management
* **Risk:** Breaking existing features during refactoring (e.g., Search stops working).
    * **Mitigation:** Ali will write unit tests for the search function immediately after refactoring to ensure stability.
* **Risk:** Documentation falling behind code changes.
    * **Mitigation:** Mohamed Ramadan will update the `refactor_log.md` continuously as Ali pushes commits.
* **Risk:** Scope creep on the "Appointment Search" feature.
    * **Mitigation:** Mohamed Jamal will ensure the feature is kept simple (search by exact date or substring name only) to meet the deadline.
