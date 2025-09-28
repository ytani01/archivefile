# Project Purpose

The `archivefile` project is a command-line utility designed to automate the archiving and renaming of files.

## Core Functionality:
- **File Movement:** Moves specified source files to a designated archive directory.
- **File Renaming:** Renames each archived file by prepending a timestamp (YYYYMMDD-HHMMSS), the original filename's root, and a user-defined status string (defaulting to 'done') before its original extension.

## Example Renaming Pattern:
If `src_file` is `my_document.txt`, `stat` is `done`, and the current time is `2025-09-28 10:30:00`, the new filename would be `20250928-103000-my_document-done.txt`.