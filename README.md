\# Diary Entry Application



A Python command-line application for creating, saving, and viewing

dated diary entries.



\## Features



\- Select a diary text file by name or path.

\- Create dated diary entries.

\- Save each entry on a separate line.

\- Display all entries in the selected diary.

\- Filter and print entries by date.

\- Load a different diary file during the session.

\- Validate dates, menu choices, and empty entries.



\## Requirements



\- Python 3

\- No third-party packages are required.



\## Run the application



Open a terminal in the project folder and run:



```bash

python main.py

```



On Windows, you can also use:



```bash

py main.py

```



\## Menu



1\. Create a diary entry

2\. View all diary entries

3\. Find diary entries by date

4\. Load a different diary file

5\. Exit



\## File structure



\- `main.py`: Application entry point and user interaction.

\- `diary.py`: Date validation, file handling, and entry filtering.



\## Diary file format



Diary files use the `.txt` extension. Each line contains one JSON

object with the entry's date and text.



Example:



```text

{"date": "2026-10-05", "text": "Today I worked on my Python assignment."}

{"date": "2026-10-06", "text": "I tested loading another diary file."}

```



Selecting an existing diary file preserves its entries.

Selecting a new file creates an empty diary.

