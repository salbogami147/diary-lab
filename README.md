# Diary Entry Application

A Python command-line application for creating, saving, and viewing dated diary entries.

## Features

- Select a diary text file by name or path.
- Create dated diary entries.
- Save each entry on a separate line.
- Display all entries in the selected diary.
- Filter and print entries by date.
- Load a different diary file during the session.
- Validate dates, menu choices, and empty entries.

## Requirements

- Python 3
- No third-party packages are required.

## Run the Application

1. Download and extract the repository.
2. Open a terminal in the folder containing `main.py` and `diary.py`.
3. Run:

   ```bash
   python main.py
   ```

   On Windows, you can also use:

   ```bash
   py main.py
   ```

4. Follow the prompts to select a diary file and use the menu.

## Menu

1. Create a diary entry.
2. View all diary entries.
3. Find diary entries by date.
4. Load a different diary file.
5. Exit.

Enter dates in `YYYY-MM-DD` format, such as `2026-10-16`.

## Project Files

| File | Purpose |
| --- | --- |
| `main.py` | Application entry point and user interaction. |
| `diary.py` | Data validation, file handling, and entry filtering. |
| `diary.txt` | Sample diary file containing entries. |
| `second_diary.txt` | Additional diary file for testing file switching. |
| `Output 1.png`–`Output 5.png` | Screenshots demonstrating application output. |

## Diary File Format

Diary files use the `.txt` extension. Each line contains one JSON object with the entry's date and text.

Example:

```json
{"date": "2026-10-05", "text": "Today I worked on my Python assignment."}
{"date": "2026-10-06", "text": "I tested loading another diary file."}
```

Selecting an existing diary file preserves its entries. Selecting a new filename creates an empty diary.
