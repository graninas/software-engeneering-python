NSU Software Engineering in Python
==================================

In this course, you’ll learn the Software Engineering and Software Design disciplines which offer several methodologies how to build applications with a predefined level of quality. You’ll know the design approaches, principles and best practices which are powered by Python but can also be translated into other languages. These principles and practices are universal and touch almost everything from the software creation process: requirements gathering, analysis, architecture design, layering, subsystems design, testing, supporting. You’ll also know about various design principles and patterns: how they help to build a testable, maintainable, reliable and robust software that satisfies the requirements. You’ll see the applicability of Python’s duck typing, OOP interfaces, functional approaches, and other elements of the language we use to express the behavior we need.

# Lecture Plan

### Recommended Literature
- “Clean Code” Robert Martin
- “Code Complete” Steve McConnell
- “Refactoring” Martin Fowler
- “Domain-Driven Design: Tackling Complexity in the Heart of Software” Eric Evans
- “Clean Architecture” Robert Martin
- “Domain Specific Languages“ Martin Fowler
- “Design Patterns: Elements of Reusable Object-Oriented Software” (aka “Gang of Four’s Book”) Erich Gamma, Richard Helm, Ralph Johnson, & John Vlissides
- “Functional Design and Architecture” Alexander Granin :)

### Part I. Software Design Basics

1. Introduction to Software Design
- Why, When, How
- The Big Picture
  - Software Lifecycle
    - Requirements Gathering & Analysis
    - Design of the Architecture
    - Design of the subsystems and components
    - Implementation, Testing
    - Deployment to Production
    - Support
  - Requirements Gathering
    - Q&A
    - Use Case diagrams (UML)
    - User Scenarios
    - Mind Maps
    - Whatever you want
  - Software Modeling
    - The Past: UML
    - The Present: whatever you want
  - Design Principles
  - Design Patterns
  - Design Approaches
  - Best Practices
  - Languages & Paradigms
  - Methodologies
- A single trick to rule them all
  - Interface (abstraction)
  - Implementation

2. Inversion of Control
- Overview
  - What is Inversion of Control principle?
  - OOP-like Interfaces
  - Functional Interfaces
- Interfaces design
  - Consistency
  - Completeness
  - Non-redundancy
  - Simplicity
  - Easy usage
  - Single Responsibility
- Dependency Injection
- IoC - сontainers

3. Layering & Modularity
- Layers by functionality
  - Domain Model
  - Business Logic
  - Application
  - Persistence
  - DB Model
  - Presentation
  - Implementation / Runtime
  - APIs, Interfaces, Domain Languages
- Pure / Impure
- Data / Logic
- Declaration / Evaluation

4. Software Reliability and Correctness
- Correctness
- Testability
- Testing practices

5. Design Principles & Patterns
- SOLID
- GRASP
- YAGNI
- KISS
- DRY
- Demetra Law, Principle of Least Power (isolation)

### Part II. Advanced Software Design

7. Design Patterns
- OOP Design Patterns
- - Task
- - Wrapper, Adapter
- - Singleton
- - Abstract Factory
- - Builder
- - Visitor
- - Interpreter
  - ...
- FP Design Patterns

6. Domain Specific Languages
- Embedded DSLs
- External DSLs (?)

8. Error Handling & Resources Management
- RAII
- Exceptions vs Errors
- “Let it Crash”
- Maybe & Either

9. Data Flow Design
- Data Flow Diagrams
- Data Flow Style
- OOP-based Data Flow Design
- FP-based Data Flow Design

10. Appendix. OOP problems
- The Circle-Ellipse (or Square-Rectangle) Problem
- The Diamond Problem
- Deep inheritance problems

---------------------------------------------------

### Control Questions 1: Interfaces, implementations, Inversion of Control

1. How did you understand what is interface in Software Engineering?
2. Provide some example of interface in Python.
3. Design an interface for objects which could report their own description to the console.
  * Provide 2 implementations of this interface. You are free to choose any business domain for this.
4. Design another interface `IPrinter` for a subsystem which can output a string to different sources.
   * Provide 2 implementations of this interface:
     - Console printer
     - File printer
   * Make `file printer` implementation configurable (think about what config it should take).
5. Rework the interface and the implementations from the 3rd paragraph so that the output source could be defined by the interface from the 4th paragraph.

### Control Questions 2: Layering
1. What do you think about layering of applications?
2. Provide a diagram. The following layers should be presented and be properly linked by one-directional arrows:
  - Business Logic
  - Implementation
  - Interfaces
3. Can you provide a rationale why the layers are related in a such way?
  
### Control Questions 3: Code practice
1. Bring the code of Math Assistant with the functionality we described on the lessons.
2. List the entities you have in your code: interfaces, implementations, functions, etc.
3. Arrange these entities on the layering diagram.
