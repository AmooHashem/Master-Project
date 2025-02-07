Below is an example of a scenario‐based lab assignment in English that meets your criteria. In this exercise, teams of two students will incrementally build a modular web application that follows atomic design principles and is containerized using Docker. Each scenario builds on the previous one, requiring you to write code, commit your changes on GitHub, and answer reflection questions.

---

# Lab Assignment: Building a Modular Web Application with Atomic Design and Docker

**Overview:**  
In this lab, you will create a simple web application using the principles of atomic design for the user interface and Docker for containerization. You will work in teams of two, use GitHub to manage your project, and follow a step-by-step scenario-based approach. Each scenario explains a new requirement; after implementing it, you will answer a reflection question regarding the concepts of modularity, Docker, or atomic design. At the end, you will submit the GitHub repository link along with a short report summarizing your design decisions and responses to the reflection questions.

---

## Scenario 1: Project Initialization and Atomic Directory Structure

**Situation:**  
Your team has been hired to design a small web application. The first step is to set up a project structure that follows atomic design principles.

**Task:**  
- Initialize a GitHub repository for your project.  
- Create a directory structure that reflects atomic design:  
  - `/src/components/atoms`  
  - `/src/components/molecules`  
  - `/src/components/organisms`  
  - `/src/components/templates`  
  - `/src/components/pages`  
- Write a `README.md` explaining the purpose of each folder and how this structure supports modular design.

**Deliverable:**  
A GitHub commit with the initialized project structure and the README file.

**Reflection Question:**  
*How does following the atomic design structure promote reusability and maintainability in UI development?*

---

## Scenario 2: Developing Atomic Components

**Situation:**  
To start building your UI, you need to create some basic, reusable elements (atoms).

**Task:**  
- Choose a front-end framework or plain HTML/CSS/JS to implement a simple "Button" component (or another basic UI element).  
- Ensure your component is self-contained, has clear props or parameters (if using a framework), and includes basic styling.  
- (Optional) Write a unit test for the component.

**Deliverable:**  
The code for your atomic component (e.g., `Button.js` or equivalent) committed to the repository.

**Reflection Question:**  
*What are the benefits of designing UI elements as atomic components in terms of modularity and reusability?*

---

## Scenario 3: Creating Composite Components with Molecules and Organisms

**Situation:**  
Now that you have a basic atomic component, it’s time to build more complex UI elements by combining atoms.

**Task:**  
- Develop a "Molecule" (for example, a login form row that uses your Button atom and an Input atom).  
- Then build an "Organism" that could represent a full "Login Section" (combining multiple molecules like a header, form, and additional information).  
- Create a simple demonstration page (e.g., an `index.html` or a small React app) that assembles these components.

**Deliverable:**  
Code for your molecule and organism components, along with a demonstration page showing the complete UI, committed to GitHub.

**Reflection Question:**  
*How does breaking down the interface into atoms, molecules, and organisms help in managing complexity in a modular system?*

---

## Scenario 4: Containerizing the Application Using Docker

**Situation:**  
To ensure that your application runs consistently across different environments, you will containerize it using Docker.

**Task:**  
- Write a `Dockerfile` that uses an appropriate base image (e.g., `node:alpine` if you’re using Node.js/React) and copies your project into the container.  
- Configure the Dockerfile to install dependencies and build/start your application.  
- Update your README with instructions on how to build and run the Docker container.

**Deliverable:**  
A working `Dockerfile` and updated documentation in your repository.

**Reflection Question:**  
*What advantages does Docker provide when deploying a modular application, and how does it support the idea of isolated, reusable modules?*

---

## Scenario 5: Enhancing Modularity Through Refactoring

**Situation:**  
With your basic application in place, your next goal is to refactor your code to further improve modularity and maintainability.

**Task:**  
- Review your components to ensure that each one has a single responsibility, clear interfaces, and minimal coupling.  
- Refactor any duplicated code (e.g., extract common functionality into helper modules or utility functions).  
- Document your refactoring process with meaningful commit messages in GitHub.

**Deliverable:**  
A series of commits showing refactored code with improved modularity, along with comments or documentation explaining the changes.

**Reflection Question:**  
*How does applying modularity principles (e.g., separation of concerns, low coupling) make your codebase easier to maintain and scale?*

---

## Scenario 6: Final Integration and Documentation

**Situation:**  
Now, integrate all the components and prepare your final submission.

**Task:**  
- Ensure that your application runs successfully from the Docker container and displays the assembled UI components correctly.  
- Write a final report (as part of your README or in a separate document) that summarizes:  
  - How atomic design was applied.  
  - How Docker helped in containerizing your modular application.  
  - The modularity improvements you implemented during refactoring.  
  - Answers to all reflection questions.

**Deliverable:**  
The final version of your project in the GitHub repository with a comprehensive README/report. Include the repository link for submission.

**Reflection Question:**  
*Summarize the overall benefits and any challenges you encountered when integrating atomic design, modularity, and Docker in this project.*

---

## Submission Instructions

1. **Work in Teams:**  
   Collaborate as a team of two throughout the experiment.

2. **Version Control:**  
   Use Git and GitHub to track your changes. Make sure to commit after each scenario with clear messages.

3. **Documentation:**  
   Update your README file to reflect the project structure, Docker instructions, and your design decisions.

4. **Final Submission:**  
   Provide the GitHub repository link along with a final report (Markdown or PDF) that includes your answers to the reflection questions.

---

This lab assignment challenges you to integrate modern software engineering practices (modularity and atomic design) with containerization (Docker) in a scenario-based, step-by-step manner. Good luck, and remember to reflect on how each concept improves the overall quality and maintainability of your application!

Would you like any additional clarifications or modifications to this experiment?