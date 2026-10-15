"""Main entry point for the diary entry application."""

from datetime import date

from diary import (
    filter_entries_by_date,
    load_entries,
    save_entry,
    select_diary_file,
    validate_date,
)


def choose_diary_file():
    """Ask the user to select a diary file."""
    while True:
        file_name = input(
            "\nEnter a diary file name or path, such as diary.txt: "
        ).strip()

        try:
            diary_path = select_diary_file(file_name)
        except (OSError, ValueError) as error:
            print(f"Could not open diary file: {error}")
        else:
            print(f"Selected diary file: {diary_path.resolve()}")
            return diary_path


def request_date(prompt, allow_today=False):
    """Request a valid date, optionally defaulting to today's date."""
    while True:
        date_text = input(prompt).strip()

        if allow_today and not date_text:
            return date.today().isoformat()

        try:
            return validate_date(date_text)
        except ValueError as error:
            print(error)


def create_entry(diary_path):
    """Collect and save a dated diary entry."""
    entry_date = request_date(
        "Enter the date (YYYY-MM-DD), or press Enter for today: ",
        allow_today=True,
    )
    entry_text = input("Write your diary entry: ").strip()

    try:
        save_entry(diary_path, entry_date, entry_text)
    except (OSError, ValueError) as error:
        print(f"Could not save entry: {error}")
    else:
        print("Diary entry saved successfully.")


def display_entries(entries):
    """Print entries in a readable format."""
    if not entries:
        print("No diary entries found.")
        return

    print("\nDiary entries")
    print("-" * 40)

    for entry in entries:
        print(f"Date: {entry['date']}")
        print(f"Entry: {entry['text']}")
        print("-" * 40)


def view_entries(diary_path, entry_date=None):
    """Load and display all entries or entries for a specified date."""
    try:
        entries, invalid_lines = load_entries(diary_path)
    except OSError as error:
        print(f"Could not read diary file: {error}")
        return

    if invalid_lines:
        line_numbers = ", ".join(str(number) for number in invalid_lines)
        print(f"Skipped incorrectly formatted lines: {line_numbers}")

    if entry_date is not None:
        entries = filter_entries_by_date(entries, entry_date)

    display_entries(entries)


def main():
    """Run the diary application's menu."""
    print("Welcome to the Diary Entry Application")
    diary_path = choose_diary_file()

    while True:
        print(f"\nCurrent diary file: {diary_path}")
        print("1. Create a diary entry")
        print("2. View all diary entries")
        print("3. Find diary entries by date")
        print("4. Load a different diary file")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            create_entry(diary_path)
        elif choice == "2":
            view_entries(diary_path)
        elif choice == "3":
            entry_date = request_date(
                "Enter the date to search (YYYY-MM-DD): "
            )
            view_entries(diary_path, entry_date)
        elif choice == "4":
            diary_path = choose_diary_file()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()