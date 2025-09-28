# Task Completion Guidelines

When a task is completed in the `archivefile` project, the following steps should be performed to ensure code quality and project integrity:

1.  **Run Linters**: Execute `ruff check .` and `flake8` to ensure all code adheres to the project's style guidelines and to catch potential errors.
2.  **Run Formatters**: Apply `ruff format .` and `isort .` to automatically format the code and sort imports, maintaining a consistent code style.
3.  **Run Type Checkers**: Use `mypy .` and `pyright` to perform static type checking and catch type-related issues.
4.  **Run Tests**: If tests are implemented, run them using `pytest` to verify that changes have not introduced regressions and that new features work as expected.
5.  **Commit Changes**: Once all checks pass, commit the changes with a clear and concise commit message that explains the purpose of the changes.
6.  **Update Documentation**: If necessary, update `README.md` or any other relevant documentation to reflect changes in functionality or usage.