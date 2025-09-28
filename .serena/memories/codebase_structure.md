# Codebase Structure

The `archivefile` project has the following key directories and files:

```
/home/ytani/work/archivefile/
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
├── uv.lock
├── .git/...
├── .mypy_cache/
├── .ruff_cache/
├── .venv/...
├── archives/                 # Default destination for archived files
├── bbb/                      # Example directory (purpose unknown without further context)
├── dist/...
├── samples/
│   └── __init__.py
├── src/
│   └── archivefile/
│       ├── __init__.py
│       ├── __main__.py       # Main entry point and CLI definition
│       ├── archivefiles.py   # Contains the core `ArchiveFiles` class and logic
│       └── __pycache__/
└── tests/
    └── __init__.py           # Placeholder for tests (no actual tests found yet)
```

## Key Files and Directories:
- **`pyproject.toml`**: Project metadata, dependencies, build system configuration, and development tools.
- **`src/archivefile/__main__.py`**: The primary script that defines the command-line interface using `click` and orchestrates the archiving process.
- **`src/archivefile/archivefiles.py`**: Contains the `ArchiveFiles` class, which encapsulates the logic for archiving and renaming individual files.
- **`archives/`**: This directory serves as the default destination for files processed by the `archivefile` utility. Files moved here are renamed with a timestamp and status prefix.
- **`tests/`**: This directory is intended for unit and integration tests. Currently, it appears to be a placeholder.