### Prompt 1: Scenario Design (Text-Based Question)

**Prompt:**  
Create a scenario-based question focusing on **clean code principles**. The question should:  

1. **Introduction**: Introduce a fictional team, organization, or project with specific roles and a realistic context for their work. Ensure the context reflects a real-world software development environment where **clean code principles** are vital.  
2. **Scenario**: Develop a realistic scenario where the team faces challenges directly tied to **clean code principles**. For example:  
   - A project with overly complex methods causing confusion during debugging.  
   - Inconsistent naming conventions across the codebase leading to misunderstandings.  
   - Legacy code with insufficient documentation making onboarding new developers difficult.  
   - A tight deadline leading to technical debt from neglecting clean coding practices.  
3. **Task**: Ask learners to complete specific tasks that directly address these challenges, such as:  
   - Propose a set of guidelines the team could adopt to ensure adherence to **clean code principles** in the future.  
   - Refactor a problematic section of code to align with **clean code principles**.  
   - Identify potential benefits for team efficiency, code maintainability, and scalability from their solutions.  
4. **Reflection and Analysis**: After completing the task, encourage learners to:  
   - Compare the situation before and after implementing clean code practices, highlighting improvements.  
   - Suggest metrics or processes the team could adopt to monitor ongoing adherence to **clean code principles**.  
   - Reflect on how clean code practices impact collaboration and long-term project success.  

**Output:**  
A detailed scenario describing the team, their project, and the specific challenges they are facing.  

---

### Prompt 2: Code Generation Based on Scenario

Using the following input, create a messy and poorly written codebase that reflects the challenges described. The codebase should:

1. Uses mock data from json files (not real backend)
2. be in pure html and css format
3. Reflect the software project described in the scenario (e.g., task management system, e-commerce platform).
4. Include intentional examples of bad practices aligned with the problems stated in the scenario:
   - Poorly named variables, functions, or classes.
   - Long, unstructured functions without clear responsibilities.
   - Code duplication and lack of modularity.
   - Inconsistent indentation or formatting.
   - Missing or excessive comments.
5. Be functional but demonstrate clear violations of clean code principles.
6. Include instructions for the learner to refactor and improve the code based on clean code principles, aligning with the issues highlighted in the scenario.

**Input:** A scenario  
**Output:** A poorly written initial codebase matching the scenario, with clear instructions for refactoring.
