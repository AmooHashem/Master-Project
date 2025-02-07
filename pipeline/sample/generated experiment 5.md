**Software Engineering Lab Experiment: Modularity, Docker, & Atomic Design**  
**Objective:** Design, containerize, and deploy a modular web application using atomic design principles, while mastering collaborative DevOps workflows.  

---

### **Lab Overview**  
**Topics:** Modularity, Docker, Atomic Design  
**Team Size:** 2 members  
**Duration:** 4-5 sessions  
**Tools:** Docker, Python/JavaScript, GitHub, Atomic Design Methodology  
**Scenario:** Students act as full-stack developers at a startup tasked with rebuilding a legacy monolithic app into a modular, Dockerized system.  

---

### **Step-by-Step Scenarios**  
#### **Scenario 1: Atomic Design Component Architecture**  
**Problem:** The legacy app’s UI is tightly coupled. Redesign it using atomic design principles.  
**Tasks:**  
1. Create a GitHub repo named `modular-app-[team-name]` with `main` and `dev` branches.  
2. Design a UI component hierarchy:  
   - **Atoms:** Buttons, Inputs  
   - **Molecules:** SearchBar (using Atoms)  
   - **Organisms:** Header (using Molecules)  
3. Implement components in separate files (e.g., `components/atoms/Button.js`).  
4. **Challenge:** A teammate accidentally deletes a shared Atom. Restore it using Git history.  
**Deliverables:**  
- Component-based UI code.  
- Git commit showing conflict resolution.  
- README section explaining atomic design structure.  

---

#### **Scenario 2: Modular Backend Services**  
**Problem:** The backend is monolithic. Split it into modular services (e.g., `auth`, `data`).  
**Tasks:**  
1. Create two Python/JS modules:  
   - `auth_service` (handles login)  
   - `data_service` (handles CRUD operations)  
2. Use REST APIs or internal method calls for inter-module communication.  
3. **Challenge:** The `auth` module fails when the `data` module is offline. Add error handling (e.g., retries).  
**Deliverables:**  
- Modular backend code with separation of concerns.  
- Unit tests for inter-module interactions.  

---

#### **Scenario 3: Dockerize Modules**  
**Problem:** Modules have conflicting dependencies. Containerize each as a standalone service.  
**Tasks:**  
1. Write individual `Dockerfiles` for `auth_service` and `data_service`.  
2. Build images and run containers for both services.  
3. **Challenge:** The `auth` container cannot connect to the `data` container. Fix using Docker networking.  
4. Use `docker-compose.yml` to orchestrate both services.  
**Deliverables:**  
- Working `Dockerfile` for each module.  
- Functional `docker-compose.yml`.  
- Screenshot of services communicating via `curl` or Postman.  

---

#### **Scenario 4: Dependency Management & Optimization**  
**Problem:** The `auth_service` image is bloated (800MB). Optimize it.  
**Tasks:**  
1. Use multi-stage builds to separate dependencies.  
2. Switch to an Alpine base image.  
3. **Challenge:** The optimized image throws a "missing library" error. Debug using `docker exec`.  
**Deliverables:**  
- Optimized `Dockerfile` (≤150MB).  
- Updated `docker-compose.yml`.  
- README explanation of optimization steps.  

---

#### **Scenario 5: CI/CD Pipeline Integration**  
**Problem:** Manual deployment is error-prone. Automate testing and builds.  
**Tasks:**  
1. Add a GitHub Actions workflow to:  
   - Run tests on PRs to `main`.  
   - Build and push images to Docker Hub on merge.  
2. **Challenge:** The pipeline fails due to flaky tests. Add retry logic.  
**Deliverables:**  
- `.github/workflows/ci-cd.yml`.  
- Screenshot of a successful pipeline run.  

---

### **GitHub Workflow Requirements**  
1. **Branching Strategy:**  
   - Use feature branches (e.g., `feature/auth-module`).  
   - Require PR reviews between teammates before merging.  
2. **Issue Tracking:**  
   - Create issues for each scenario (e.g., “Fix Docker networking”).  
   - Close issues via PRs with keywords (e.g., “Fixes #2”).  
3. **Commit Hygiene:**  
   - Atomic commits with descriptive messages.  
   - Tag commits by scenario (e.g., `git tag scenario-3`).  

---

### **Documentation & Reflection**  
1. **README.md:**  
   - Setup instructions for the app and Docker.  
   - Explanation of atomic design hierarchy.  
   - Lessons learned (e.g., “Avoiding circular dependencies in modules”).  
2. **Reflection Log:**  
   - A `REFLECTION.md` file detailing:  
     - Technical debt encountered (e.g., “Temporary workaround for Redis timeout”).  
     - Git collaboration challenges (e.g., “Resolved merge conflict in `docker-compose.yml`”).  

---

### **Evaluation Criteria**  
| **Criteria**                 | **Points** |
| ---------------------------- | ---------- |
| Atomic Design Implementation | 20         |
| Modularity & Separation      | 20         |
| Docker Configuration         | 25         |
| Git Collaboration & Workflow | 15         |
| Documentation & Reflection   | 20         |

**Total:** 100 points  

---

### **Submission Guidelines**  
1. **Final Repository Link:** Submit the GitHub URL with:  
   - All code, Dockerfiles, and CI/CD workflows.  
   - Commit history showing incremental progress.  
   - Closed issues and PRs.  
2. **Tagged Releases:** Create a release tag `v1.0` after completing all scenarios.  

---

**Instructor Notes:**  
- Use GitHub Insights to track collaboration patterns.  
- Conduct a code review session focusing on modularity and Docker best practices.  
- Highlight real-world parallels (e.g., “This mirrors how Netflix decomposes its services”).  

**Scenario Conclusion:** Students will master modular design, containerization, and collaborative DevOps practices, preparing them for scalable, maintainable software engineering.