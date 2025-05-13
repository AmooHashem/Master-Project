Below is a comprehensive lab experiment plan that guides teams of two students through the entire Community CMS project. The plan is broken down into sequential stages that mirror the scenario’s narrative. Each stage includes clear tasks, coding checkpoints, collaboration guidelines, and reflective prompts. The estimated total work time is at least 8 person-hours (roughly 4 hours per team).

---

# **Lab Experiment Plan: Building a Community-Driven CMS with Git**

---

## **Pre-Lab Preparation**

1. **Team Formation & Environment Setup:**
   - **Form Teams:** Pair up with one other student.
   - **Install Tools:** Ensure that Git is installed on your local machine, and sign up for a Git hosting service (e.g., GitHub, GitLab).
   - **Editor Setup:** Choose your preferred code editor (e.g., VS Code, Sublime Text).

2. **Review the Scenario:**
   - Read through the provided Community CMS scenario.
   - Familiarize yourself with each stage’s objectives and specific conditions.

3. **Documentation Template:**
   - Create a shared document (e.g., a Google Doc or Markdown file in your repository) to record:
     - Decisions made at each stage.
     - Challenges encountered and how they were resolved.
     - Reflection notes after completing each stage.

---

## **Stage 1: Project Setup & Repository Initialization**

### **Objective:**
Establish a clean, well-documented starting point for the project using basic Git operations.

### **Tasks:**

1. **Repository Creation:**
   - **Local Repository:**  
     - Initialize a new git repository in a dedicated project folder.
     - Create a basic directory structure, for example:
       ```
       community-cms/
         ├── src/
         ├── docs/
         ├── tests/
         └── README.md
       ```
   - **Remote Repository:**  
     - Create a repository on GitHub (or your chosen platform) and link it as the remote for your local repository.

2. **Initial Commit:**
   - Add all initial project files.
   - Write a descriptive commit message (e.g., “Initial commit: Set up project structure and documentation”).
   - **Command Example:**
     ```bash
     git add .
     git commit -m "Initial commit: Set up basic project structure"
     git push -u origin main
     ```

3. **Documentation & .gitignore:**
   - Edit `README.md` to include:
     - Project title, purpose, and instructions for cloning the repository.
     - Contribution guidelines.
   - Create a `.gitignore` file to exclude unnecessary or sensitive files (e.g., environment files, OS-specific files).

4. **Checkpoint:**
   - **Review:** Check the commit history with `git log` and ensure the repository is properly set up.
   - **Reflection:** Write a brief note in your documentation about your initial setup process, what went well, and any questions you have.

**Estimated Duration:** 1 Hour

---

## **Stage 2: Feature Branch Development & Basic Merging**

### **Objective:**
Develop the initial version of the blog user interface on a separate feature branch, practice making incremental commits, and resolve a simulated merge conflict.

### **Tasks:**

1. **Create Feature Branch:**
   - From the main branch, create and switch to a new branch named `feature/blog-ui`.
   - **Command Example:**
     ```bash
     git checkout -b feature/blog-ui
     ```

2. **Implement Blog UI:**
   - Develop a basic front-end for displaying blog posts (e.g., create HTML/CSS/JavaScript files under the `src/` directory).
   - **Coding Task:**  
     - Design a simple layout that includes a header, a list of blog posts, and a footer.
     - Create at least one file (e.g., `src/blog.html`) with placeholder content.

3. **Incremental Commits:**
   - Commit your work in small steps:
     - **Commit 1:** Initial creation of blog UI layout.
     - **Commit 2:** Add styling (simulate a minor bug fix by updating a CSS rule).
   - **Command Example:**
     ```bash
     git add .
     git commit -m "Add initial blog UI layout"
     git commit -m "Fix minor styling bug in blog UI"
     ```

4. **Simulate and Resolve a Merge Conflict:**
   - **Simulate:**  
     - From the main branch, edit a shared file (e.g., update a line in `README.md` or a common configuration file).
     - In parallel, have a change in the same line on the `feature/blog-ui` branch.
   - **Merge Attempt:**  
     - Try merging `feature/blog-ui` back into main.
     - When a conflict appears, open the conflicting file, and manually resolve the differences.
   - **Commands Example:**
     ```bash
     # On main branch, simulate change:
     git checkout main
     echo "Update from main branch" >> README.md
     git commit -am "Simulate change in README from main branch"
     
     # Switch back and attempt merge:
     git checkout feature/blog-ui
     git merge main  # Resolve conflict manually
     git add <resolved_file>
     git commit -m "Resolve merge conflict between main and feature/blog-ui"
     git checkout main
     git merge feature/blog-ui
     git push
     ```

5. **Checkpoint:**
   - **Review:** Compare branch histories using `git log --graph --oneline`.
   - **Documentation:** Record the steps you took to resolve the merge conflict and note any challenges.
   
**Estimated Duration:** 1.5 Hours

---

## **Stage 3: Collaborative Branching & Conflict Resolution**

### **Objective:**
Split into sub-teams to develop user authentication and administrative tools concurrently, practice pull requests, code reviews, and resolve merge conflicts in a team setting.

### **Tasks:**

1. **Branching for Parallel Development:**
   - **Sub-team A:** Create branch `feature/user-auth` for registration, login, and session management.
   - **Sub-team B:** Create branch `feature/admin-panel` for administrative content management.
   - **Command Example (run in parallel by each sub-team):**
     ```bash
     git checkout -b feature/user-auth   # For Sub-team A
     git checkout -b feature/admin-panel # For Sub-team B
     ```

2. **Simultaneous Feature Development:**
   - **User Authentication:**  
     - Implement a simple registration form and login page in `src/auth.html` (or separate files as preferred).
   - **Admin Panel:**  
     - Develop a basic admin interface in `src/admin.html` that includes content management options.
   - **Coding Guidelines:**  
     - Commit incremental changes with clear messages.  
     - Ensure each sub-team updates and tests their respective feature.

3. **Simulate Merge Conflict:**
   - Both branches should modify a common file (e.g., a configuration file `config.js` or a shared utility module in `src/utils.js`).
   - Intentionally edit the same line in each branch to simulate a conflict.

4. **Pull Requests & Code Reviews:**
   - Push both branches to the remote repository.
   - **Create Pull Requests (PRs):**  
     - Submit PRs for merging `feature/user-auth` and `feature/admin-panel` into the main branch.
   - **Peer Reviews:**  
     - Each sub-team reviews the other’s PR, providing constructive feedback through comments.
   - **Resolve Conflicts:**  
     - Collaboratively merge the branches into main, resolving any conflicts in the shared file(s).

5. **Checkpoint:**
   - **Review:** Use GitHub’s PR interface and local testing to ensure the features integrate smoothly.
   - **Documentation:**  
     - Record the conflict resolution process.
     - Reflect on the benefits and challenges of working concurrently on overlapping files.

**Estimated Duration:** 1.5 Hours

---

## **Stage 4: Advanced Git Techniques & History Management**

### **Objective:**
Clean up the repository history using advanced Git techniques to maintain a coherent and understandable commit log.

### **Tasks:**

1. **Interactive Rebase:**
   - On one of your feature branches (e.g., `feature/blog-ui`), use interactive rebase (`git rebase -i`) to squash related commits.
   - **Task Example:**  
     - Combine commits that pertain to the initial UI layout into a single, well-documented commit.
   - **Command Example:**
     ```bash
     git checkout feature/blog-ui
     git rebase -i main
     # Follow on-screen instructions to squash commits.
     ```

2. **Reverting Faulty Commits:**
   - Identify a commit that introduced a bug (this can be simulated if needed).
   - Use `git revert` to create a new commit that undoes the problematic changes.
   - **Command Example:**
     ```bash
     git log  # Find the commit hash to revert
     git revert <commit-hash>
     git push
     ```

3. **Cherry-Picking:**
   - Identify a useful change from one branch (e.g., a layout improvement) that is not yet in another branch.
   - Use `git cherry-pick` to apply that commit to another branch.
   - **Command Example:**
     ```bash
     git checkout feature/admin-panel
     git cherry-pick <commit-hash>
     git push
     ```

4. **Checkpoint:**
   - **Review:** Use `git log` to verify that the commit history is now cleaner and easier to follow.
   - **Documentation:**  
     - Write down the commands used and the rationale behind each advanced technique.
     - Reflect on how these techniques can improve collaboration and repository maintainability.

**Estimated Duration:** 1 Hour

---

## **Stage 5: Integrating External Contributions & Release Management**

### **Objective:**
Manage external contributions, conduct thorough reviews, and simulate a release process with tagging and hotfixes.

### **Tasks:**

1. **Simulate External Contributions:**
   - **Pull Request 1:**  
     - Simulate receiving a PR for a new feature (e.g., integration of social media sharing) by creating a branch (e.g., `external/social-share`) and adding the feature in a new file (e.g., `src/social.html`).
   - **Pull Request 2:**  
     - Simulate a PR that fixes a critical bug in an existing file (e.g., `src/blog.html`).

2. **Review & Integration:**
   - **Review Process:**  
     - Each team member should review the changes in these PRs, comment on code quality, and suggest improvements.
   - **Testing:**  
     - Pull the changes locally and test them before merging.
   - **Merge:**  
     - Merge the PRs into the main branch after ensuring they meet project standards.

3. **Release Tagging & Hotfix:**
   - **Tagging:**  
     - Once external contributions are merged, tag the repository with a version number (e.g., `v1.0.0`).
     - **Command Example:**
       ```bash
       git tag v1.0.0
       git push origin v1.0.0
       ```
   - **Hotfix Simulation:**  
     - If a post-release bug is identified, create a hotfix branch (e.g., `hotfix/issue-001`), fix the bug, commit the changes, and merge it back into main.
     - **Command Example:**
       ```bash
       git checkout -b hotfix/issue-001
       # Fix the bug in the relevant file(s)
       git commit -am "Fix post-release bug: issue-001"
       git checkout main
       git merge hotfix/issue-001
       git push
       ```

4. **Checkpoint:**
   - **Review:** Verify that the release tag appears in the commit history and that the hotfix branch is correctly merged.
   - **Documentation:**  
     - Document the review process and the release management steps.
     - Reflect on the challenges of integrating external contributions and managing releases.

**Estimated Duration:** 1 Hour

---

## **Final Reflection & Submission Guidelines**

### **Reflection:**
- **Prompt:**  
  Write a reflective document (e.g., `REFLECTION.md`) that covers:
  - **Challenges Encountered:**  
    - Discuss difficulties with merge conflicts, branching strategies, and history management.
  - **Solutions & Best Practices:**  
    - Describe the steps taken to resolve conflicts and maintain a clean commit history.
    - Highlight best practices adopted during collaboration.
  - **Lessons Learned:**  
    - Reflect on how these experiences will influence your future approach to software development and Git workflows.
    - Mention any additional Git techniques or tools you’d like to explore.

### **Submission Guidelines:**
- **Repository Organization:**  
  - Ensure your repository is well-organized with clear directories (e.g., `src/`, `docs/`).
  - Include a detailed `README.md` that explains the project setup, branch strategies, and how to run the application.
- **Documentation:**  
  - Commit all documentation files (e.g., `README.md`, `REFLECTION.md`, and any additional notes).
- **Final Submission:**  
  - Push all commits to your remote repository.
  - Submit the GitHub repository link to your instructor via the designated submission portal.
  - Confirm that all branches have been merged or appropriately documented.

---

## **Summary & Time Allocation**

- **Stage 1:** Project Setup & Repository Initialization – **~1 Hour**
- **Stage 2:** Feature Branch Development & Basic Merging – **~1.5 Hours**
- **Stage 3:** Collaborative Branching & Conflict Resolution – **~1.5 Hours**
- **Stage 4:** Advanced Git Techniques & History Management – **~1 Hour**
- **Stage 5:** Integrating External Contributions & Release Management – **~1 Hour**
- **Reflection & Submission:** Documentation and final submission – **~30 Minutes**

---

By following this detailed lab experiment plan, you and your teammate will gain hands-on experience with Git operations, learn how to manage concurrent development, and understand advanced techniques for maintaining a clean project history. The process emphasizes collaboration, critical thinking, and reflective learning to simulate real-world software development challenges. Enjoy the process and happy coding!