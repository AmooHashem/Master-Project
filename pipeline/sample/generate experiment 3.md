Below are two separate prompts. The first prompt asks for the creation of a realistic scenario (the “scenario creator”), and the second prompt uses that scenario as input to design a complete lab experiment (the “lab experiment designer”).

---

### **Prompt 1: Scenario Creator**

**Objective:**  
Create a detailed, multi-stage scenario that will serve as the foundation for a scenario-based software engineering lab experiment. This scenario should incorporate the following two inputs:

1. **Topic(s):**  
   *[Insert the topic or topics here—for example, 'Git Workflow Optimization', 'Dependency Management & Build Tools', or 'Managing Pull Requests with Git'.]*

2. **Extra Learning Objectives:**  
   *[Insert the extra learning objectives here. These might include concepts such as Git commands (e.g., fetching, checking out branches, merging, using pull request refs), best practices in handling pull requests and Git aliases, dependency management guidelines (e.g., using dedicated build/dependency tools over Git, splitting large repositories, using submodules as an alternative), and insights on caching in build systems.]*

**Instructions:**  
- **Meaningful Project:**  
  Frame the scenario around a meaningful project that will engage the students.
  
- **Realistic Context & Progressive Challenges:**  
  Structure the scenario into a series of realistic, interconnected situations. Each situation should present a clear problem statement or condition that the students must analyze and solve through coding. Ensure that each stage builds upon the previous one by:
  - Introducing new challenges.
  - Gradually increasing in complexity.
  
- **Incorporate Extra Learning Objectives:**  
  Ensure that each extra teaching point has addressed in at least one of the scenarios.
  
- **Reflection Opportunity:**  
  End the scenario with a prompt for reflection where the teams must document the challenges they faced and how they addressed issues.

**Deliverable:**  
Output a fully developed scenario that is structured in multiple stages. Each stage should include:
- A clear problem statement.
- Specific conditions or constraints.

---

### **Prompt 2: Lab Experiment Designer**

**Objective:**  
Using the scenario provided as input, design a comprehensive, step-by-step lab experiment. This experiment should guide teams of two students through the entire process of solving the scenario.

**Instructions:**  
- **Step-by-Step Breakdown:**  
  Develop a detailed plan that breaks down the experiment into several sequential steps. Each step should correspond to a stage in the provided scenario and include:
  - A clear description of the task.
  - Specific coding tasks.
  - Checkpoints where students must commit their changes, compare diffs, or perform refactoring.
  
- **Scenario-Based Tasks:**  
  For each stage of the scenario, provide:
  - A clear problem statement or condition.
  - Detailed instructions on how to analyze the problem, design a solution using appropriate software engineering principles, and implement the solution via code.
  
- **Team Collaboration & GitHub Integration:**  
  Specify how the teams should:
  - Collaborate using Git (e.g., splitting tasks, conducting peer reviews, merging branches).
  - Organize their work in a GitHub repository, with incremental commits and clear commit messages that reflect the work done.
  
- **Estimated Duration & Complexity:**  
  Ensure that the entire experiment requires a minimum of 8 person-hours (approximately 4 hours per team). To achieve this:
  - Include sufficiently complex tasks that require thoughtful problem solving.
  - Introduce multiple steps, such as initial setup, coding, testing, iterative improvement, etc.
  Avoid including any details about the total time required for the experiment or for each individual section.

- **Documentation & Reflection:**  
  Require that at each step, students:
  - Document their approach.
  - Reflect on any challenges encountered.
  
- **Final Submission Guidelines:**  
  Provide detailed guidelines on how to:
  - Organize the repository.
  - Document progress in a README or dedicated documentation file.
  - Submit the final GitHub repository link to the instructor, ensuring all commits are pushed and all tasks are clearly documented.

**Deliverable:**  
Create a complete lab experiment plan that:
- Uses the input scenario as the underlying narrative.
- Provides clear, step-by-step instructions for each stage of the experiment.
- Outlines specific coding tasks and checkpoints.
- Emphasizes documentation and reflection.

---

By using these two prompts, you first generate a detailed scenario and then build a lab experiment around it that meets the specified educational objectives and workflow requirements.