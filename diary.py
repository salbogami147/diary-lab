"""Functions for storing and reading dated diary entries."""

import json
from datetime import datetime
from pathlib import Path


def validate_date(date_text):
    """Validate a date and return it in YYYY-MM-DD format."""
    try:
        parsed_date = datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError as error:
        raise ValueError(
            "Enter a valid date in YYYY-MM-DD format."
        ) from error

    formatted_date = parsed_date.strftime("%Y-%m-%d")

    if date_text != formatted_date:
        raise ValueError("Use YYYY-MM-DD format, such as 2026-10-05.")

    return formatted_date


def select_diary_file(file_name):
    """Create or open a diary text file without deleting existing entries."""
    if not file_name.strip():
        raise ValueError("The file name cannot be empty.")

    diary_path = Path(file_name.strip()).expanduser()

    if diary_path.suffix.lower() != ".txt":
        raise ValueError("The diary file must have a .txt extension.")

    # Append mode creates a missing file and preserves an existing file.
    with diary_path.open("a", encoding="utf-8"):
        pass

    return diary_path


def save_entry(diary_path, entry_date, entry_text):
    """Append one diary entry as one line in the selected text file."""
    entry_date = validate_date(entry_date)
    entry_text = entry_text.strip()

    if not entry_text:
        raise ValueError("A diary entry cannot be empty.")

    entry = {
        "date": entry_date,
        "text": entry_text,
    }

    with diary_path.open("a", encoding="utf-8") as diary_file:
        diary_file.write(json.dumps(entry, ensure_ascii=False) + "\n")


def load_entries(diary_path):
    """Read diary entries and report any incorrectly formatted lines."""
    entries = []
    invalid_lines = []

    with diary_path.open("r", encoding="utf-8") as diary_file:
        for line_number, line in enumerate(diary_file, start=1):
            if not line.strip():
                continue

            try:
                entry = json.loads(line)

                if not isinstance(entry, dict):
                    raise ValueError("Entry must be an object.")

                validate_date(entry["date"])

                if not isinstance(entry["text"], str):
                    raise ValueError("Entry text must be a string.")

                if not entry["text"].strip():
                    raise ValueError("Entry text cannot be empty.")

            except (ValueError, KeyError, TypeError):
                invalid_lines.append(line_number)
                continue

            entries.append(entry)

    return entries, invalid_lines


def filter_entries_by_date(entries, entry_date):
    """Return entries matching the requested date."""
    entry_date = validate_date(entry_date)

    return [
        entry
        for entry in entries
        if entry["date"] == entry_date
    ]