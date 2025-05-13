# Git and Version Control Lab Experiment  
**Course:** Software Engineering Laboratory  
**Topic:** Git & Version Control  
**Duration:** Approximately 2–3 hours  
**Submission:** Provide a link to your GitHub repository containing the completed project with all commit history.

---

## **Overview**

In this lab, you will simulate a real-world software development scenario where version control is essential. You will work step-by-step through a series of challenges, each presented as a scenario. At every step, you must solve the problem (by applying your Git knowledge), write the necessary code or documentation, and commit your work. This lab will help you practice:

- Initializing and setting up a repository
- Branching and merging
- Handling merge conflicts
- Documenting changes and progress

Each step is designed to be completed in sequence. To earn credit for a step, you must demonstrate that you have successfully completed the task—typically via commit messages, branch names, or updated documentation in your GitHub repository.

---

## **Lab Scenario and Steps**

### **Step 1: Repository Initialization & Baseline Commit**

**Scenario:**  
Your team has just been assigned a new project. As the team’s repository manager, your first task is to set up the project's repository.

**Tasks:**

1. **Initialize the Repository:**
   - Create a new GitHub repository named `git-version-control-lab`.
   - Clone the repository locally.

2. **Create the Baseline Project Structure:**
   - In your local repository, create a folder structure that includes:
     - A `README.md` file (with a brief project description).
     - A `src/` directory for source code.
     - A `docs/` directory for documentation.
   - Write a brief introduction in the `README.md`.

3. **Commit and Push:**
   - Commit all the initial files with a clear commit message (e.g., "Initialize repository with baseline structure").
   - Push the commit to GitHub.

**Verification:**
- Check your GitHub repository to ensure that the structure is correctly set up and the commit history shows the initial commit.

---

### **Step 2: Branching for a New Feature**

**Scenario:**  
The product owner has requested a new feature: a simple script that prints "Hello, World!" to the console. To keep your work organized, you need to create a feature branch.

**Tasks:**

1. **Create a Feature Branch:**
   - From the `main` branch, create a new branch called `feature/hello-world`.

2. **Implement the Feature:**
   - In the `src/` directory, create a new file (e.g., `hello_world.py` for Python, or `helloWorld.js` for JavaScript) that contains code to print "Hello, World!".
   - Add comments in your code explaining your implementation.

3. **Commit and Push:**
   - Commit your changes with a message like "Add hello world feature".
   - Push the `feature/hello-world` branch to GitHub.

**Verification:**
- Verify on GitHub that the new branch exists and the file with the new feature is present.

---

### **Step 3: Merging and Conflict Resolution**

**Scenario:**  
While you were working on your feature branch, another team member (simulated by you) updated the `README.md` on the `main` branch with additional project details. Now, you need to merge the `main` branch into your feature branch and resolve any conflicts that may arise.

**Tasks:**

1. **Simulate a Conflict:**
   - On the `main` branch, edit the `README.md` to add a new section called "Project Overview". Commit and push these changes.

2. **Merge Main into Feature:**
   - Switch back to your `feature/hello-world` branch.
   - Merge the `main` branch into your feature branch.
   - If conflicts occur (likely in `README.md`), resolve them manually ensuring both your changes and the new project overview are retained.
  
3. **Commit the Merge:**
   - Once conflicts are resolved, commit the merge with a descriptive message (e.g., "Merge main into feature/hello-world and resolve conflicts").

**Verification:**
- Check that your `feature/hello-world` branch includes both the updated `README.md` and the hello world feature file.
- The commit history should reflect the merge and conflict resolution.

---

### **Step 4: Final Integration and Documentation**

**Scenario:**  
Now that your feature is complete and up to date with the latest changes, it's time to merge your work back into `main` and finalize your project documentation.

**Tasks:**

1. **Merge Feature Branch into Main:**
   - Open a Pull Request (PR) from `feature/hello-world` to `main` on GitHub.
   - In your PR description, summarize the changes and steps taken.
   - Merge the PR into `main` after ensuring that all checks have passed.

2. **Document the Process:**
   - Update the `docs/` folder by creating a file (e.g., `lab_report.md`) that explains:
     - The project setup.
     - The steps you took during the lab.
     - How you handled branching, merging, and conflict resolution.
   - Commit and push this documentation update to `main`.

3. **Final Submission:**
   - Verify that your GitHub repository now has all the changes in the `main` branch.
   - Ensure that your commit history reflects all the steps described in the lab.

**Verification:**
- The final `main` branch should contain:
  - The complete project structure.
  - The `README.md` with the project overview.
  - The feature code file in `src/`.
  - The lab documentation in `docs/`.
- The commit history should clearly outline each step taken.

---

## **Submission Instructions**

1. **Repository Link:**  
   Provide the GitHub repository URL that contains all your work.

2. **Commit History:**  
   Ensure that your commit history on GitHub shows clear, descriptive messages for each step of the lab.

3. **Lab Report:**  
   The documentation in the `docs/` folder should reflect your understanding and actions during each scenario.

---

## **Additional Tips**

- **Commit Often:** Make small, meaningful commits at each step.
- **Clear Messages:** Write commit messages that clearly explain the purpose of the commit.
- **Test Your Code:** Before committing, run your code to ensure it works as expected.
- **Backup:** If needed, push your changes to a temporary branch before performing merge operations.