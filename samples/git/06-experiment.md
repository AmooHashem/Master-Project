Below is a complete lab experiment plan that uses the *Project Aurora* scenario as its narrative. This plan is designed to guide teams of two students through a multi-stage process—from initial repository setup and branching strategy to release engineering and final reflections. Each stage contains detailed instructions, coding tasks, Git checkpoints, and documentation requirements to ensure a comprehensive learning experience.

---

# **Lab Experiment: Project Aurora – Smart Building IoT Integration Platform**

---

## **Overview**

In this lab, you will collaboratively develop and manage a multi-module IoT platform. Your tasks include setting up your Git repository with an effective branching strategy, developing features via pull requests and code reviews, integrating a CI/CD pipeline, managing large digital assets with Git LFS/git-annex, and finally, preparing the project for release with robust disaster recovery strategies. At every step, you are required to document your approach and reflect on any challenges encountered.

**Team Collaboration & GitHub Integration:**  
- **Split Tasks:** Divide work between modules (e.g., IoT sensors, web dashboard, mobile app, firmware assets) and share responsibilities for configuration, testing, and documentation.
- **Git Workflow:** Use feature branches, commit frequently with clear messages, create pull requests (PRs) for review, and merge following code review guidelines.
- **Documentation:** Maintain a clear README (or separate documentation file) that outlines your branching strategy, development process, and decisions at each stage.
- **Submission:** Your final submission will include the complete Git repository (with all commits pushed), the CI/CD configuration files, and a final report that summarizes challenges, solutions, and lessons learned.

---

## **Stage 1: Project Initialization & Branching Strategy**

### **Problem Statement:**
Set up a central Git repository that supports concurrent development across multiple modules, and document your branching and merging strategy.

### **Tasks & Instructions:**

1. **Repository Setup:**
   - **Task:** Initialize a central repository (on GitHub or another hosting service).
   - **Instructions:**
     - Create a protected `main` (or `master`) branch.
     - Set up branch protection rules (e.g., require pull requests and passing CI tests before merging).
     - Document these settings in the README.
   - **Checkpoint:** Commit an initial README that outlines your project description and branching strategy.

2. **Creating Feature Branches:**
   - **Task:** Create initial feature branches for each module:
     - `feature/iot-sensors`
     - `feature/web-dashboard`
     - `feature/mobile-app`
     - `feature/firmware`
   - **Instructions:**
     - Use Git commands to create and push these branches.
     - Document in your README the purpose of each branch and how they will be used.
   - **Checkpoint:** Commit your branch creation process (e.g., screenshots or Git log output).

3. **Agile Process Integration:**
   - **Task:** Define iteration/sprint goals for incremental development.
   - **Instructions:**
     - Outline at least one sprint goal per module.
     - Add these details in a separate `SprintPlan.md` file.
   - **Checkpoint:** Commit the `SprintPlan.md` file.

4. **Commit Standards & Milestones:**
   - **Task:** Establish guidelines for commit messages and use Git tags to mark milestones.
   - **Instructions:**
     - Include a section in the README on how to write descriptive commit messages.
     - Decide on key milestones (e.g., after initial module development, after CI/CD integration) and plan to tag these in Git.
   - **Checkpoint:** Commit an update to the README reflecting these standards.

---

## **Stage 2: Feature Development, Pull Request Management & Code Review**

### **Problem Statement:**
Develop features concurrently, manage pull requests, and implement a systematic code review process.

### **Tasks & Instructions:**

1. **Feature Branch Development:**
   - **Task:** On each feature branch, add initial code or configuration files specific to the module.
   - **Instructions:**
     - For example, on `feature/iot-sensors`, create a basic script or configuration that simulates sensor data collection.
     - On `feature/web-dashboard`, add a placeholder HTML/JavaScript file.
     - Commit changes with clear messages.
   - **Checkpoint:** Verify the creation of feature-specific files via Git diff and commit logs.

2. **Pull Request Workflow:**
   - **Task:** Create pull requests when a feature is ready for review.
   - **Instructions:**
     - Each team member opens a PR from their feature branch to `main` (or to an integration branch if preferred).
     - Use Git’s commenting features to discuss code changes and resolve conflicts.
   - **Checkpoint:** Document a PR discussion thread (or a summary in your documentation) that highlights how code review was handled.

3. **Git Aliases & PR References:**
   - **Task:** Create Git aliases to automate fetching and checking out pull request references.
   - **Instructions:**
     - Create an alias (e.g., in your `.gitconfig`) to fetch all PR branches from the remote.
     - Demonstrate how to fetch a specific PR locally (e.g., using a command like `git fetch origin pull/ID/head:pr-branch`).
     - Document these commands in a `GitCommands.md` file.
   - **Checkpoint:** Commit the updated `.gitconfig` and the `GitCommands.md`.

4. **Integration of Code Quality Tools:**
   - **Task:** Integrate a static analysis tool (e.g., ESLint, SonarQube) and a testing framework.
   - **Instructions:**
     - Set up configuration files (e.g., `.eslintrc.json`) and write at least one simple test case for one module.
     - Document the code review checklist and guidelines in a file named `CodeReviewGuidelines.md`.
   - **Checkpoint:** Commit the configuration files and guidelines document.

---

## **Stage 3: DevOps Integration & CI/CD Pipeline Implementation**

### **Problem Statement:**
Automate the build, test, and deployment process by integrating a CI/CD pipeline.

### **Tasks & Instructions:**

1. **CI/CD Pipeline Setup:**
   - **Task:** Choose a CI/CD tool (e.g., GitHub Actions, GitLab CI) and configure it.
   - **Instructions:**
     - Create a pipeline configuration file (e.g., `.github/workflows/ci-cd.yml`).
     - Ensure the pipeline triggers on new commits and merged PRs.
     - Include steps for static analysis, running unit/integration tests, and deploying to a staging environment.
   - **Checkpoint:** Commit the CI/CD configuration file and verify that the pipeline runs successfully with sample commits.

2. **Automation of Branch Merging:**
   - **Task:** Set up the pipeline to perform automated merging upon successful tests.
   - **Instructions:**
     - Integrate scripts that check for test pass status and merge feature branches automatically (if applicable).
     - Document how the automation is configured.
   - **Checkpoint:** Commit the automation scripts and add notes in your documentation.

3. **Monitoring & Error Reporting:**
   - **Task:** Configure notifications or error reporting within the CI/CD system.
   - **Instructions:**
     - Set up email or Slack notifications for build failures.
     - Document troubleshooting steps in your documentation.
   - **Checkpoint:** Commit a README update that includes these monitoring details.

---

## **Stage 4: Managing Large Digital Assets with Git LFS / git-annex**

### **Problem Statement:**
Manage large binary files (e.g., sensor firmware updates and high-resolution security images) using Git LFS or git-annex.

### **Tasks & Instructions:**

1. **Identify Large Assets:**
   - **Task:** Determine which file types (e.g., `.bin`, `.img`) should be managed with Git LFS/git-annex.
   - **Instructions:**
     - List these file types and add the configuration in your documentation.
   - **Checkpoint:** Commit an updated `.gitattributes` file that tracks the designated file types.

2. **Tool Integration:**
   - **Task:** Set up Git LFS (or git-annex) to track large assets.
   - **Instructions:**
     - Install Git LFS and run commands such as `git lfs track "*.bin"`.
     - Provide instructions in a file (`LargeAssetGuide.md`) on how to clone and fetch these assets.
   - **Checkpoint:** Commit the `.gitattributes` and `LargeAssetGuide.md` files.

3. **Versioning and Testing:**
   - **Task:** Ensure that the large assets are versioned in sync with your code.
   - **Instructions:**
     - Make a change to a large asset and verify that Git LFS/git-annex updates correctly.
     - Document the update and retrieval process.
   - **Checkpoint:** Commit and tag this change as a milestone.

---

## **Stage 5: Release Engineering & Disaster Recovery**

### **Problem Statement:**
Prepare the project for its first major release while implementing robust disaster recovery and rollback strategies.

### **Tasks & Instructions:**

1. **Release Management Process:**
   - **Task:** Develop and document a release process.
   - **Instructions:**
     - Create a script or a documented process for version tagging (e.g., `v1.0.0`), writing release notes, and deploying to production.
     - Use Git’s tagging features to mark stable releases.
     - Add this information to a file named `ReleaseProcess.md`.
   - **Checkpoint:** Commit the `ReleaseProcess.md` and create a Git tag for a stable commit.

2. **Rollback Strategies:**
   - **Task:** Implement rollback strategies in case of failed deployments.
   - **Instructions:**
     - Write scripts that allow quick reversion to a previous commit.
     - Document a step-by-step disaster recovery plan, including simulated scenarios (e.g., corrupted data).
     - Add this to a file named `DisasterRecoveryPlan.md`.
   - **Checkpoint:** Commit the rollback scripts and disaster recovery documentation.

3. **Testing Release and Recovery:**
   - **Task:** Simulate a release failure scenario.
   - **Instructions:**
     - Trigger a controlled failure (e.g., push a commit with an intentional error) and then execute your rollback strategy.
     - Document the process and outcomes in your final report.
   - **Checkpoint:** Commit logs and notes that summarize the test results.

---

## **Stage 6: Reflection & Documentation**

### **Problem Statement:**
Reflect on the project journey by analyzing challenges, solutions, and process improvements.

### **Tasks & Instructions:**

1. **Final Report:**
   - **Task:** Write a comprehensive final report that reflects on your entire project process.
   - **Instructions:**
     - Address the challenges encountered at each stage, focusing on branching strategies, pull request management, CI/CD integration, and disaster recovery.
     - Explain how Git refs/refspecs, Git aliases, and local testing of pull requests streamlined your workflow.
     - Discuss your experience managing large assets with Git LFS or git-annex.
     - Evaluate the effectiveness of your disaster recovery and rollback strategies.
     - Reflect on how Agile practices and continuous integration influenced your development process and suggest improvements for future iterations.
   - **Checkpoint:** Save the report as `FinalReport.md` and commit it to the repository.

2. **Documentation Consolidation:**
   - **Task:** Ensure all configuration files, scripts, and guides are well-documented and organized.
   - **Instructions:**
     - Verify that the README includes an overview of the project structure, branching strategy, CI/CD setup, and release process.
     - Review and update all documentation files to ensure clarity and consistency.
   - **Checkpoint:** Make a final commit that consolidates all documentation updates.

3. **Final Submission Guidelines:**
   - **Task:** Prepare your repository for submission.
   - **Instructions:**
     - Ensure that all commits are pushed to the remote repository.
     - Verify that your repository contains:
       - All configuration and code files.
       - CI/CD configuration and logs.
       - Documentation files (`README.md`, `SprintPlan.md`, `GitCommands.md`, `CodeReviewGuidelines.md`, `LargeAssetGuide.md`, `ReleaseProcess.md`, `DisasterRecoveryPlan.md`, and `FinalReport.md`).
     - Submit the GitHub repository link to your instructor.

---

## **Summary of Checkpoints and Deliverables**

- **Initial Setup:**  
  - Repository initialization, branch protection rules, README, and sprint plan.
- **Feature Development:**  
  - Feature branches, PRs, Git alias configuration, static analysis, and testing configuration.
- **CI/CD Pipeline:**  
  - CI/CD configuration file(s), automation scripts, and documentation on monitoring.
- **Large Asset Management:**  
  - `.gitattributes` file for Git LFS, detailed guide for handling large assets.
- **Release & Recovery:**  
  - Release process documentation, rollback scripts, and simulated disaster recovery test logs.
- **Final Documentation:**  
  - A comprehensive final report and all other documentation files consolidated in the repository.

---

This lab experiment plan is intended to simulate a real-world development environment, where collaboration, version control, continuous integration, and effective release engineering are essential. Be sure to document every step of your process and reflect on what you learn as you progress. Good luck, and enjoy the journey of building *Project Aurora*!