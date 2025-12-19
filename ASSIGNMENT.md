
# Software Maintenance & Evolution — Capstone Mini-Project (Clinic Legacy System)

## Project summary
You will work in teams of **3** to maintain, refactor, and evolve a small legacy-like Clinic web app (Flask). The provided codebase is intentionally messy: global state, duplicated functions, tight coupling between domain objects, no tests, and minimal documentation. Your task is to apply the course concepts to improve the system and document the process.

---
## Learning objectives
- Identify maintenance types: corrective, adaptive, perfective, preventive.
- Measure software using LOC, Function Points (approx), and make effort estimates using COCOMO (basic).
- Plan maintenance work using Agile (user stories, backlog) or a linear maintenance plan.
- Apply refactoring and/or reengineering to improve maintainability.
- Demonstrate software evolution by adding one small feature or improving behavior.
- Compare metrics before and after changes and justify decisions.

---
## Getting started (student instructions)
1. Clone or unzip the project.
2. Create a Python virtual environment and install requirements:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open http://127.0.0.1:5000 in your browser.

---
## Phases & Deliverables (teams)
1. **Analysis (Week 1)**  
   - Deliverable: `analysis.md` — short report describing the codebase, issues (coupling/cohesion, duplication, missing tests), and initial LOC count.
2. **Metrics & Estimation (Week 1)**  
   - Deliverable: `metrics.md` — LOC (use `wc -l` or manual), Function Point estimate (approx), and a simple COCOMO-based effort/time estimate. Document assumptions.
3. **Maintenance Plan (Week 2)**  
   - Deliverable: `plan.md` — backlog of user stories, sprint plan (2 sprints), and assignment of tasks within team (3 people).
4. **Implementation (Week 3-4)**  
   - Deliverable: `repo/` — refactored code in a Git repo with commits. Include `refactor_log.md` showing before/after snapshots and explanations for each major change.
   - Implement one **evolution** change (choose one): improve appointment search, add patient notes export (CSV), add basic validation, or convert appointments to reference patient_id instead of patient object.
5. **Evaluation (Week 4)**  
   - Deliverable: `evaluation.md` — recompute LOC, complexity (qualitative), and demonstrate how maintainability improved (or where it didn't). Include screenshots and test commands.
6. **Final Presentation (Week 5)**  
   - Deliverable: 10-minute recorded demo + `final_report.pdf` (or markdown) and link to Git repo.

---
## Suggested tasks (pick at least 4)
- Remove duplicated helpers and centralize patient functions.
- Replace global state with a simple repository class or module.
- Add input validation to forms and show error messages.
- Convert appointment storage to reference patient_id (reduce coupling).
- Add unit tests for 5–8 functions using pytest (extra credit).
- Add logging and a basic README for developers.

---
## Grading rubric
- Analysis & metrics accuracy: 20%
- Maintenance plan & user stories: 15%
- Quality of refactoring & implementation: 30%
- Evolution feature: 15%
- Documentation, git history, and reflection: 15%
- Teamwork & presentation: 5%

---
## Constraints & Notes for students
- Keep changes small and incremental; show clear before/after evidence.
- You may use external libraries but justify them.
- Keep the UI simple — focus is maintenance and code quality, not design.
- Preserve original app behavior where not explicitly improved — mention any behavior changes in report.
