# Backend Calculator

A calculator application that performs operations and keeps a history of all calculations. Built with Python and file-based storage.


## Program requirements

 * Perform basic operations (addition, subtraction, multiplication, division) on two numbers
* store the history of all operations performed, including the inputs, operation type, and result
* Handle all possible edge cases, ideally never fully crashing
* have a method that returns the full history of operations performed,  the time taken to perform each operation and the timestamp of when the operation was performed.
* Have an help method that explains how to use the app and what it can do.

<br><hr>

### Technical Constraints

- Use **uv** for package management
- Use **classes** to model your data (e.g. an operation, a result, a history entry)
- Use **Enum** to define the set of valid  mathematical operations
- Use **files** (JSON, CSV, or TXT — your choice) to persist data instead of a database
- Validate all input data and return appropriate error messages when the input is invalid

<br>
<hr>
<br>

## Guide

<br>

Choose one of two paths depending on your comfort level:

- **Path A (CLI)** — No server, no HTTP. You run the program from the terminal with flags.
- **Path B (API)** — A web API built with Flask.


### Setup


```bash
uv sync
```
---

### Run the app

----

### Path A — CLI

```bash
uv run python main.py --action=calculate --operation=3,plus,9
uv run python main.py --action=get-history
```

### Path B — API

```bash
uv run flask run
```

### Usecases

#### 1. Perform a Calculation

Accepts two numbers and an operation, performs the calculation, stores it in the history, and returns the result.

**Path A:**
```bash
uv run python main.py --action=calculate --operation=3,plus,9
# Output: 3 + 9 = 12
```

**Path B:** A POST endpoint that accepts two numbers and an operation in the request body and returns the result.

The minimum set of supported operations:

- Addition
- Subtraction
- Multiplication
- Division

#### 2. Get Calculation History

Returns a list of all operations that have been performed, including the inputs, operation type, and result.

**Path A:**
```bash
uv run python main.py --action=get-history
```

**Path B:** A GET endpoint that returns the full history.

#### 3. Help

Add an help endpoint or action that returns information about the app, the author, and what it can do.
<br>

## Bonus

### Bonus 1

- **Unit testing** — write tests for your calculation logic
- **Edge cases** — think about what could go wrong and handle it (what happens when you divide by zero? what if the operation doesn't exist? what if the numbers aren't numbers?)

### Bonus 2

- **Composed operations** — how would you support expressions like `(2 + 3) * 4 / 2`?
*  Using github actions, set up a workflow that runs your tests on every push to the repository or every pull request

<br>
