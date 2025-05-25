## **Lab Experiment Plan: Online Payment Processing System**

### **Overview**
Students work in teams of two to build a modular, scalable, and well-documented online payment processing system. The lab is divided into multiple stages that address:
- **Stage 1:** Analysis & Code Smell Identification  
- **Stage 2:** Refactoring for Encapsulation & Abstraction  
- **Stage 3:** Introducing Inheritance & Polymorphism via a PaymentGateway Interface  
- **Stage 4:** Advanced Refactoring & Integration (Dependency Injection and Configuration Management)  
- **Stage 5:** Testing, Documentation, and Peer Review  
- **Stage 6:** Reflection and Final Submission

Each stage contains specific coding tasks, checkpoints for commits, and reflective documentation steps to ensure continuous learning and team collaboration.

---

### **Stage 1: Initial Analysis & Code Smell Identification**

**Objective:**  
Analyze the monolithic payment module (provided as starter code) to identify design flaws and violations of SOLID principles.

**Tasks:**
- **Code Review:**  
  - Read through the provided monolithic code that handles payment validation, processing, and external gateway integration.
  - Identify issues such as high coupling, long methods, duplicated code, and unclear responsibilities.

- **Documentation:**  
  - Create a report (or add inline comments) listing identified code smells.
  - Note which SOLID principles are violated (e.g., Single Responsibility, Open/Closed, etc.).

- **Checkpoint:**  
  - Commit your findings and a summary report to a branch called `stage1-analysis` with a commit message like “Stage 1: Documented code smells and SOLID violations.”

**Team Collaboration:**  
- Split the review task: one teammate reads the code while the other creates a checklist for SOLID principles.
- Use a shared document (e.g., README.md update or separate analysis file) to record findings.

---

### **Stage 2: Refactoring for Encapsulation & Abstraction

**Objective:**  
Refactor the monolithic module by introducing an abstract `Payment` class and concrete subclasses for each payment method (e.g., `CreditCardPayment`, `DigitalWalletPayment`, `BankTransferPayment`).

**Tasks:**
- **Design and Code:**  
  - Create an abstract class `Payment` with common attributes (e.g., amount, currency, timestamp) and a method `validatePayment()`.
  - Develop subclasses that override or extend `validatePayment()` and add any specific behavior.
  - Separate payment processing logic from third-party API integration.

- **Documentation:**  
  - Add inline comments and generate initial Javadoc/Doxygen comments for the new classes.
  - Update your project documentation (e.g., in README.md) to reflect the new architecture.

- **Checkpoint:**  
  - Commit changes to a branch called `stage2-refactor` with clear commit messages (e.g., “Stage 2: Added Payment abstraction and concrete subclasses”).

**Team Collaboration:**  
- Divide tasks by assigning one teammate to design the abstract class and the other to implement specific payment types.
- Review each other’s commits using GitHub’s pull request (PR) mechanism.

---

### **Stage 3: Inheritance & Polymorphism with PaymentGateway Interface

**Objective:**  
Design and implement a `PaymentGateway` interface to decouple gateway integrations from the core payment logic.

**Tasks:**
- **Design the Interface:**  
  - Define a `PaymentGateway` interface with methods such as `processPayment()`, `refundPayment()`, and `getTransactionStatus()`.

- **Implement Concrete Gateways:**  
  - Create at least two classes (e.g., `StripeGateway` and `PayPalGateway`) that implement the interface.
  - Where possible, use inheritance to share common functionality (e.g., a base class `BaseGateway`).

- **Polymorphism:**  
  - Modify the payment processing system to accept any implementation of the `PaymentGateway` interface.
  - Demonstrate usage by switching gateway implementations at runtime.

- **Documentation:**  
  - Document the interface and its implementations with inline comments and design diagrams if desired.

- **Checkpoint:**  
  - Commit changes to a branch named `stage3-gateway` with messages like “Stage 3: Introduced PaymentGateway interface and concrete implementations.”

**Team Collaboration:**  
- One teammate can focus on designing and documenting the interface, while the other implements the concrete gateway classes.
- Use pair programming sessions to test polymorphic behavior together.

---

### **Stage 4: Integration and Advanced Refactoring

**Objective:**  
Decouple external dependencies and enhance configuration management using advanced refactoring and dependency injection.

**Tasks:**
- **Dependency Injection:**  
  - Refactor the system so that external payment gateways are injected rather than hard-coded.  
  - Create a configuration manager to load sensitive configuration details (API keys, endpoint URLs) from secure files or environment variables.

- **Code Isolation:**  
  - Separate concerns: isolate payment processing, gateway integration, and configuration management into distinct modules.
  - Update the design to use clearly defined interfaces between modules.

- **Documentation:**  
  - Update all design documents and inline comments to explain how dependency injection and configuration management have been implemented.

- **Checkpoint:**  
  - Commit changes to a branch named `stage4-integration` with a commit message like “Stage 4: Applied dependency injection and externalized configuration.”

**Team Collaboration:**  
- Work together to choose a DI framework or implement a simple DI container.
- Use GitHub Issues and PR reviews to ensure that configuration management does not leak sensitive data.

---

### **Stage 5: Testing, Documentation, and Final Review

**Objective:**  
Ensure the system works as intended through comprehensive testing and create detailed documentation.

**Tasks:**
- **Test Development:**  
  - Write unit tests for each class (especially for `Payment` subclasses and PaymentGateway implementations).
  - Develop integration tests simulating scenarios (e.g., payment failures, network timeouts, refund operations).

- **Documentation:**  
  - Generate full documentation (using Javadoc/Doxygen) and update the project README to describe system architecture, design choices, and testing strategies.
  - Document your Git commit history and include a “CHANGELOG” file that summarizes major changes across stages.

- **Peer Review:**  
  - Conduct a code review session with your teammate to ensure that refactoring adheres to object-oriented and SOLID principles.
  - Add a peer review report (a separate Markdown file) summarizing improvements and any further potential enhancements.

- **Checkpoint:**  
  - Commit your test cases and documentation improvements on a branch named `stage5-testing-docs`.

**Team Collaboration:**  
- Split the testing tasks so that one teammate focuses on unit tests and the other on integration tests.
- Use GitHub’s PR review features to provide feedback on each other’s test code and documentation.

---

### **Stage 6: Reflection and Final Submission**

**Objective:**  
Reflect on the refactoring process, challenges encountered, and lessons learned. Prepare the final submission.

**Tasks:**
- **Reflection Report:**  
  - Write a final report covering:
    - The main challenges during refactoring.
    - How applying abstraction, encapsulation, inheritance, and polymorphism reduced complexity.
    - The benefits of introducing interfaces for testability and modularity.
    - The effectiveness of testing strategies and suggestions for future improvements.
  - Include reflections on teamwork and GitHub collaboration (e.g., branch strategies, code reviews).

- **Final Repository Organization:**  
  - Ensure your GitHub repository includes separate folders for source code, tests, documentation, and the reflection report.
  - Make sure all branches have been merged into a `main` branch.
  - Clean up commit messages if needed for clarity.

- **Submission Guidelines:**  
  - Push all changes and ensure the final repository link is submitted.
  - Include a detailed README.md outlining:
    - Project overview and architecture
    - Step-by-step changes per stage
    - Instructions to run tests and build the project
    - Your reflection report summary

- **Checkpoint:**  
  - Final commit on the `main` branch with a message like “Final Submission: Completed all stages, documentation, and reflection.”

**Team Collaboration:**  
- Discuss as a team the lessons learned and record each team member’s contributions.
- Use a shared document (or collaborative markdown file) for the reflection report and commit it to the repository.

---

## **Additional Guidelines & Best Practices**

- **Time Management:**  
  - Work iteratively, ensuring that each stage builds on the previous one.
  - Make sure to commit frequently and use clear, descriptive commit messages.

- **Git/GitHub Integration:**  
  - Use feature branches for each stage (e.g., `stage1-analysis`, `stage2-refactor`, etc.).
  - Conduct regular code reviews using GitHub pull requests.
  - Resolve merge conflicts collaboratively.

- **Documentation & Reflection:**  
  - Keep an updated project log or diary that notes decisions, challenges, and lessons learned after each stage.
  - Use inline comments and generate external documentation to support your design decisions.

- **Collaboration & Peer Review:**  
  - Schedule brief meetings after each stage to compare diffs, discuss challenges, and plan next steps.
  - Each team member should review the other's code and provide constructive feedback.

- **Final Submission:**  
  - Organize the repository so that it is easy for an instructor to navigate.
  - Include a final README with sections on project overview, development process, and reflection.
  - Submit the GitHub repository link as instructed by your instructor.
