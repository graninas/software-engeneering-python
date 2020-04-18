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

6. Design Patterns
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

7. Domain Specific Languages & Domain Driven Development
- Domain Driven Development
- Embedded DSLs
- External DSLs

8. Error Handling
- Defensive programming
- Exceptions and Errors
  * Exceptions vs Errors
  * Exception hierarchies
  * Error domains
  * nulls vs optionals vs None
  * Handling techniques
    - try/catch
    - Maybe & Either
    - Continuations
    - Make invalid cases unrepresentable
  * Failure to list of successes
- The “Let it Crash” philosophy
- Bugs are not errors and exceptions

9. Resources Management
- Constructors and destructors
- RAII
- Handling resources in multithreaded environment

10. Data Flow Design
- Fluent Interface
- Data Flow Diagrams
- Data Flow Style
- OOP-based Data Flow Design
- FP-based Data Flow Design

11. Appendix. OOP problems
- The Circle-Ellipse (or Square-Rectangle) Problem
- The Diamond Problem
- Deep inheritance problems

---------------------------------------------------

# Math Assistant

### Functional Requirements
* Knowledge Base with math objects which have name and description.
* Command-line application
* CLI Commands:
  - `Finish`: finish the CLI application
    `finish`
  - `Describe`: describe a notion from the Knowledge Base
    `describe <name:str>
    `describe "Number"`
  - `Add`: add a notion into the Knowledge Base
    `add <name:str> <descr:str>`
    `add "some name" "some description"

# Labyrinth

* Implement the "Labyrinth" game (aka "Terra Incognita").
  - [Labyrinth (Wiki)](https://en.wikipedia.org/wiki/Labyrinth_(paper-and-pencil_game))
  - [Terra Incognita](https://www.thegamecrafter.com/games/terra-incognita)
* You should use the knowledge obtained during the course.
* Design the game using:
  - Interfaces (OOP-like)
  - Inversion of Control
  - Dependency Injection
  - Proper layering
  - Proper project structure
  - Diagrams of classes and interaction between classes
* The code should be extensible enough to support new upcoming requirements (see "Mandatory set of rules" and "Extended set of rules").

### Functional requirements

* "Labyrinth" is a one-player turn-by-turn game which should be implemented as a console application.
  - Game consists of labyrinth, labyrinth objects, user inventory, CLI interface.
  - Computer is a master of game.
  - Game is controlled by text commands.
  - Initially, the player can't see the labyrinth. The player should explore the labyrinth on its own.
* User commands:
  - Starting a new game with a predefined labyrinth size: "start <labyrinth_size>". Labyrinth size should be not less 4 and not bigger 10.
  - Quiting the current game: "quit" (without saving).
  - Quiting the current game with saving: "save <file_name>" (the game should be saved into a text file).
* On the start, labyrinth should be randomly generated.
  - Labyrinth consists of cells.
  - A wall can be built between any two neighbour cells.
  - An outside wall is called monolith.
  - There should be no inaccessible cells.
  - There should be one exit randomly dislocated in the monolith wall.

##### Mandatory set of rules

* Game flow:
  - Player's goal to find a treasure and leave the labyrinth.
  - Games starts after the labyrinth is generated.
  - On the start, player is invited to enter commands.
  - Game prints the results of processing the commands.
  - Game ends when the player leaves the labyrinth with a treasure.
  - If the player doesn't have a treasure found, the game should say he can't leave the labyrinth on attempt to pass through the exit.
* Game objects:
  - Treasure.
  - 5 wormholes, organized into a cyclic ordered set. Entering a wormhole moves the player into the next wormhole by index. Skipping a move while staying on the wormhole moves the player to the next wormhole.
* User commands:
  - Moving: "go up", "go down", "go left", "go right".
  - Skipping a turn: "skip".
* Game messages:
  - "step impossible, wall"
  - "step executed, wormhole"
  - "step executed, treasure"
  - "step impossible, monolith"
  - "step executed" (on successful moving)

##### Extended set of rules

* Game objects:
  - River. Has source and end. Several cells arranged in a chain which cannot intersect itself.
    Entering a river moves the player 2 cells down a stream (maximum).
    Skipping a turn triggers this moving again.
    River and wormholes cannot share the same cell.
  - Bear. Bear is like a player but moves randomly and is NPC.
    River and wormholes affect bear as well.
    Once bear and player step on the same cell, player becomes damaged.
    When damaged, the player should be also moved 1 cell away from the bear towards any passable direction.
    (If this is not possible, player stays where he was)
    Damaging the player second time makes him dead.
  - Map. When the player has a map he can use the "map" command to see the whole labyrinth
    (including treasure, bear, river, wormholes).
    Using this command behaves like skipping a turn (all the effects should be applied.)

---------------------------------------------------

# Control work

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
