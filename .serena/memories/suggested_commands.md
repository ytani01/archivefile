# Suggested Commands

This section outlines essential commands for developing, testing, and running the `archivefile` project.

## Project Entrypoint
- **Run the `archivefile` command:**
  ```bash
  archivefile <src_files> [options]
  ```
  *Example: `archivefile my_file.txt --stat processed --dstdir /tmp/archived`*

## Development Commands

### Linting
- **Run Ruff linter:**
  ```bash
  ruff check .
  ```
- **Run Flake8 linter:**
  ```bash
  flake8
  ```

### Formatting
- **Run Ruff formatter:**
  ```bash
  ruff format .
  ```
- **Run iSort (import sorting):**
  ```bash
  isort .
  ```

### Type Checking
- **Run MyPy type checker:**
  ```bash
  mypy .
  ```
- **Run Pyright type checker:**
  ```bash
  pyright
  ```

### Testing
- **Run tests (assuming pytest is configured):**
  ```bash
  pytest
  ```
  *(Note: No `tests` directory was found with explicit test files, so `pytest` is a common assumption. Verify if tests exist and how they are run.)*

## Utility Commands
Standard Linux utility commands are available, such as:
- `git` (for version control)
- `ls` (list directory contents)
- `cd` (change directory)
- `grep` (search text)
- `find` (find files)
- `cat` (concatenate and display files)
- `less` (file viewer)