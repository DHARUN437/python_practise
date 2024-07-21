def display_menu():
    print("Note-Taking Application")
    print("1. View notes")
    print("2. Add a new note")
    print("3. Search for a note by title")
    print("4. Delete a note")
    print("5. Exit")

def view_notes(notes):
    if not notes:
        print("No notes available.")
    else:
        for title, content in notes.items():
            print(f"Title: {title}\nContent: {content}\n")

def add_note(notes):
    title = input("Enter the note title: ")
    content = input("Enter the note content: ")
    if title in notes:
        print("A note with this title already exists.")
    else:
        notes[title] = content
        print("Note added successfully.")

def search_note(notes):
    title = input("Enter the title of the note to search: ")
    if title in notes:
        print(f"Title: {title}\nContent: {notes[title]}")
    else:
        print("Note not found.")

def delete_note(notes):
    title = input("Enter the title of the note to delete: ")
    if title in notes:
        del notes[title]
        print("Note deleted successfully.")
    else:
        print("Note not found.")

def main():
    notes = {}
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            search_note(notes)
        elif choice == '4':
            delete_note(notes)
        elif choice == '5':
            print("Exiting the Note-Taking Application.")
            break
        else:
            print("Invalid choice. Please try again.")
        
        input("Press Enter to continue...")  # Pause for user to press Enter before continuing
        print()  # Add a new line for better readability in the loop

if __name__ == "__main__":
    main()
