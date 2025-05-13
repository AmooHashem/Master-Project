# **Git, Version Control & Dependency Management Lab**

**Course:** Software Engineering Laboratory  
**Topic:** Git Version Control, Dependency Management, and Repository Organization  
**Duration:** Approximately 3–4 hours  
**Submission:** Provide a link to your GitHub repository containing the complete project with all commit history and documentation.

---

## **Overview**

In this lab, you will simulate managing a software project that is evolving from a single large repository to a more modular, maintainable structure. You will work step-by-step through various scenarios that illustrate best practices and challenges regarding:
  
- **Project Dependencies:** Recognizing that dependencies should be managed by dedicated build/dependency tools rather than Git.
- **Repository Splitting:** Deciding when and how to split a large repository into logical components.
- **Git Submodules:** Using submodules when a dedicated dependency tool is not an option.
- **Workflow with Git:** Branching, merging, and documenting your progress.

For each scenario, you will use Git commands to implement the required changes and demonstrate the underlying concepts with clear commit messages and supporting documentation.

---

## **Lab Scenarios and Steps**

### **Step 1: Repository Initialization & Baseline Setup**

**Scenario:**  
You have joined a new project. Your first task is to set up the initial repository structure and demonstrate the proper management of dependencies using a build tool.

**Tasks:**

1. **Initialize the Repository:**
   - Create a new GitHub repository named `dependency-management-lab`.
   - Clone the repository locally:
     ```bash
     git clone https://github.com/your-username/dependency-management-lab.git
     cd dependency-management-lab
     ```

2. **Establish Project Structure:**
   - Create the following structure:
     - `README.md` (explain the project and mention that dependencies will be managed by a dedicated tool)
     - `src/` (source code directory)
     - `build/` (simulate a build tool configuration directory)
     - `docs/` (for lab documentation)
   - **Dependency Management:**  
     Create a build configuration file (e.g., `build/dependencies.txt`) that lists dependencies.  
     *Guideline to note:*  
     > "Project Dependencies Should Not Be Managed with Git if possible. Use a dedicated tool to manage them."  
     Add a comment in `README.md` explaining the rationale.

3. **Commit and Push:**
   - Commit your initial setup:
     ```bash
     git add .
     git commit -m "Initialize repository with project structure and dependency management guidelines"
     git push origin main
     ```

**Verification:**  
- The repository on GitHub should display the correct folder structure and a README that outlines the dependency management strategy.

---

### **Step 2: Simulating Repository Splitting**

**Scenario:**  
As the project grows, the build times increase, and dependencies become shared across several modules. The project owner has decided to split the repository into smaller, logical components.

**Tasks:**

1. **Create a New Branch for Repository Splitting:**
   - Create and switch to a branch named `split-repo`:
     ```bash
     git checkout -b split-repo
     ```

2. **Simulate Splitting the Project:**
   - Move some source files from `src/` into a new folder named `modules/core/` to represent the core component.
   - Create another folder `modules/feature/` for a new feature that depends on the core component.
   - Update `README.md` to include a note on why splitting is beneficial:
     > “Once a project grows over a certain size, it makes sense to split it into logical components.”
   - Create a document in `docs/` called `splitting_challenges.md` outlining the challenges of splitting a project (e.g., release delays, manual build setups, discoverability issues).

3. **Commit and Push:**
   - Commit your changes:
     ```bash
     git add .
     git commit -m "Split project into core and feature modules and document challenges"
     git push origin split-repo
     ```

**Verification:**  
- Verify that the repository now contains separate modules and that the documentation explains the reasons and challenges of splitting a repository.

---

### **Step 3: Introducing Git Submodules**

**Scenario:**  
Not all parts of the project can use a dedicated dependency tool. For some legacy components, you must integrate external code via Git submodules.

**Tasks:**

1. **Decide Which Module Uses a Submodule:**
   - For example, assume the `feature` module relies on a legacy library that is maintained in a separate Git repository.
  
2. **Add a Git Submodule:**
   - Add the legacy library as a submodule inside `modules/feature/legacy_lib`:
     ```bash
     git submodule add https://github.com/legacy-org/legacy-library.git modules/feature/legacy_lib
     ```
   - Ensure that the submodule is set to track a stable release branch (e.g., `release`).

3. **Document Submodule Usage:**
   - In `docs/`, create a file named `submodule_usage.md` that describes when and why you chose to use a submodule over a dependency tool:
     > “If you can't or don't want to use a dependency tool, you may use Git submodules as an alternative.”
  
4. **Commit and Push:**
   - Commit all changes, including the updated `.gitmodules` file:
     ```bash
     git add .
     git commit -m "Integrate legacy library as a submodule and document its usage"
     git push origin split-repo
     ```

**Verification:**  
- Verify that the submodule appears in your repository structure and that documentation clearly explains its purpose and configuration.

---

### **Step 4: Feature Branch and Final Integration**

**Scenario:**  
A new feature needs to be developed that interacts with both the core module and the feature module. You must create a feature branch, implement the changes, and then merge it back into your main branch.

**Tasks:**

1. **Create a Feature Branch:**
   - From the `split-repo` branch, create a new branch called `feature/new-functionality`:
     ```bash
     git checkout -b feature/new-functionality
     ```

2. **Implement the Feature:**
   - In `modules/feature/`, add a new file (e.g., `new_feature.py`) that interacts with the core module.
   - Document the changes in `README.md` and update `docs/feature_documentation.md` explaining the new functionality.
  
3. **Commit and Push:**
   - Commit your feature changes:
     ```bash
     git add .
     git commit -m "Implement new feature integrating core and feature modules"
     git push origin feature/new-functionality
     ```

4. **Merge Feature into Main:**
   - Open a Pull Request (PR) on GitHub from `feature/new-functionality` into `split-repo`.
   - After review, merge the PR and then merge `split-repo` back into `main` (or create a final integration branch if required).

**Verification:**  
- Verify on GitHub that the new feature appears in the integrated branch, and all documentation and commit messages reflect the changes.

---

### **Step 5: Final Documentation and Submission**

**Scenario:**  
You need to ensure that all your actions, decisions, and the rationale behind them are clearly documented.

**Tasks:**

1. **Consolidate Documentation:**
   - In the `docs/` folder, update or create a file named `lab_report.md` that includes:
     - An explanation of why dependencies should be managed with dedicated tools.
     - The benefits and challenges of splitting a repository.
     - When to use Git submodules versus dependency tools.
     - The steps you took to implement the changes.
  
2. **Final Commit:**
   - Commit your final documentation:
     ```bash
     git add docs/lab_report.md
     git commit -m "Add comprehensive lab report documenting dependency management and repository splitting"
     git push origin main
     ```

3. **Submission:**
   - Provide the GitHub repository URL to your instructor.

**Verification:**  
- Ensure that your repository contains clear commit history, all lab files, and a comprehensive lab report that explains your decisions and workflow.

---

## **Additional Tips**

- **Frequent Commits:** Commit small, logical changes often to document your progress.
- **Descriptive Messages:** Use detailed commit messages to explain your reasoning.
- **Test Your Changes:** Run tests (if applicable) to ensure that the build configurations and submodule integrations work as expected.
- **Review Documentation:** Make sure your documentation is clear, concise, and covers the concepts from the extracted teaching points.
