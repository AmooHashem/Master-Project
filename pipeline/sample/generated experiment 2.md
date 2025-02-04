### **Git and Version Control - Scenario-Based Lab**  
**Course:** Software Engineering Laboratory  
**Topic:** Advanced Git & Version Control for Collaborative Development  
**Duration:** Approximately 2–3 hours  
**Submission:** Provide a link to your GitHub repository containing the completed project with all commit history.  

---

## **Overview**  

In this lab, you will simulate working as a software developer in a collaborative environment. You will interact with a shared repository, handle pull requests, manage branches, and optimize your workflow using Git commands. Each step presents a real-world development scenario where you must solve a problem, execute the necessary Git operations, and document your work through commits.  

This lab focuses on:  

- Fetching and checking out remote branches  
- Handling pull requests efficiently  
- Managing multiple remotes and forks  
- Using Git aliases for workflow optimization  

Each step is sequential, and you must demonstrate the correct execution by committing your work and maintaining a clear commit history.  

---

## **Lab Scenario and Steps**  

### **Step 1: Setting Up the Repository and Initial Configuration**  

**Scenario:**  
You have joined a development team that uses Git for version control. Your first task is to set up the project repository locally and configure Git for efficient collaboration.  

**Tasks:**  

1. **Clone the Shared Repository:**  
   - Clone the repository from GitHub or Bitbucket:  
     ```bash
     git clone https://github.com/your-org/git-collab-lab.git
     ```
   - Navigate into the project directory:  
     ```bash
     cd git-collab-lab
     ```

2. **Fetch and List All Remote Branches:**  
   - Fetch all branches from the remote repository:  
     ```bash
     git fetch origin
     ```
   - List available remote branches:  
     ```bash
     git branch -r
     ```

3. **Verify Repository Configuration:**  
   - Check the remote URL and repository details:  
     ```bash
     git remote -v
     git config --list
     ```
   - Commit any necessary changes to the README file, adding your name as a contributor.  

**Verification:**  
- Push the updated `README.md` with your name to the `main` branch and verify that it appears in the commit history.  

---

### **Step 2: Working with a Feature Branch and Handling PRs**  

**Scenario:**  
You have been assigned a new feature (`PRJ-1234`). Your task is to check out this feature branch, make modifications, and prepare it for review via a pull request.  

**Tasks:**  

1. **Check Out the Feature Branch:**  
   - Create and switch to a local branch tracking the remote feature branch:  
     ```bash
     git checkout -b PRJ-1234 origin/PRJ-1234
     ```

2. **Implement the Feature:**  
   - Modify the `src/main.py` file (or equivalent) to add a simple function.  
   - Add comments explaining the feature.  

3. **Commit and Push:**  
   - Commit the changes with a meaningful message:  
     ```bash
     git commit -am "Implement feature PRJ-1234 - added new function"
     ```
   - Push the feature branch to GitHub:  
     ```bash
     git push origin PRJ-1234
     ```

**Verification:**  
- Ensure the `PRJ-1234` branch appears on GitHub with your changes.  

---

### **Step 3: Handling a Forked Repository and Managing Multiple Remotes**  

**Scenario:**  
A contributor has forked the repository and made changes to their version. You need to fetch and review their work.  

**Tasks:**  

1. **Add the Contributor’s Repository as a Remote:**  
   - Add the forked repository as a remote:  
     ```bash
     git remote add jsmith https://bitbucket.org/jsmith/coolproject.git
     ```
   - Verify the remote was added successfully:  
     ```bash
     git remote -v
     ```

2. **Fetch the Contributor’s Branches:**  
   - Fetch branches from the contributor’s fork:  
     ```bash
     git fetch jsmith
     ```

3. **Check Out the Contributor’s Work Locally:**  
   - Check out their feature branch locally:  
     ```bash
     git checkout -b jsmith-PRJ-1234 jsmith/PRJ-1234
     ```

**Verification:**  
- Ensure you can see and test the contributor’s code locally.  

---

### **Step 4: Reviewing and Merging a Pull Request**  

**Scenario:**  
You have reviewed a contributor’s pull request and need to merge it into the `main` branch after ensuring it is up-to-date.  

**Tasks:**  

1. **Fetch and Merge the Latest Changes from Main:**  
   - Switch to the `main` branch:  
     ```bash
     git checkout main
     ```
   - Fetch and merge the latest changes:  
     ```bash
     git fetch origin
     git merge main
     ```

2. **Merge the Contributor’s Feature Branch:**  
   - Merge the `jsmith-PRJ-1234` branch into `main`:  
     ```bash
     git merge jsmith-PRJ-1234
     ```

3. **Resolve Any Merge Conflicts (If Needed):**  
   - If conflicts arise, resolve them manually, then commit the merge.  

4. **Push the Merged Changes to GitHub:**  
   - Push the updated `main` branch:  
     ```bash
     git push origin main
     ```

**Verification:**  
- Ensure the contributor’s work is now part of the `main` branch and is reflected in the repository history.  

---

### **Step 5: Optimizing Workflow with Git Aliases**  

**Scenario:**  
To streamline the pull request review process, you will configure Git aliases for fetching pull requests more efficiently.  

**Tasks:**  

1. **Create an Alias to Fetch a Single PR (Bitbucket):**  
   ```bash
   git config alias.spr '!sh -c "git fetch origin pull-requests/${1}/from:pr/${1}" -'
   ```

2. **Create an Alias to Fetch a Single PR (GitHub):**  
   ```bash
   git config alias.gpr '!sh -c "git fetch origin pull/${1}/head:pr/${1}" -'
   ```

3. **Use the Alias to Fetch a PR:**  
   - Fetch PR #102 using the alias:  
     ```bash
     git gpr 102
     ```

**Verification:**  
- Ensure the alias correctly fetches the PR into a local branch.  

---

## **Final Submission**  

1. **GitHub Repository:**  
   - Submit the repository URL with all completed tasks and commit history.  

2. **Commit History:**  
   - Ensure all changes are clearly documented in meaningful commit messages.  

3. **Documentation:**  
   - Update the `docs/` folder with a file (`git_lab_report.md`) summarizing:  
     - The Git commands used.  
     - Steps taken in each scenario.  
     - Any challenges encountered and how they were resolved.  

---

## **Additional Tips**  

- **Commit Frequently:** Make small, meaningful commits for clarity.  
- **Use Descriptive Messages:** Ensure commit messages explain the purpose clearly.  
- **Verify Changes Before Pushing:** Use `git status` and `git log` to confirm expected modifications.  
