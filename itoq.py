import json
from datetime import datetime

class NotesApp:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.filename, 'r') as file:
                notes = json.load(file)
            return notes
        except FileNotFoundError:
            return []

    def save_notes(self):
        with open(self.filename, 'w') as file:
            json.dump(self.notes, file, indent=2)

    def display_notes(self):
        if not self.notes:
            print("No notes available.")
        else:
            for note in self.notes:
                print(f"ID: {note['id']}, Title: {note['title']}, Created: {note['created_at']}")

    def add_note(self, title, body):
        note = {
            'id': len(self.notes) + 1,
            'title': title,
            'body': body,
            'created_at': str(datetime.now())
        }
        self.notes.append(note)
        self.save_notes()
        print(f"Note added successfully. ID: {note['id']}")

    def read_note(self, note_id):
        note = next((n for n in self.notes if n['id'] == note_id), None)
        if note:
            print(f"ID: {note['id']}, Title: {note['title']}, Body: {note['body']}, Created: {note['created_at']}")
        else:
            print("Note not found.")

    def edit_note(self, note_id, title, body):
        note = next((n for n in self.notes if n['id'] == note_id), None)
        if note:
            note['title'] = title
            note['body'] = body
            note['edited_at'] = str(datetime.now())
            self.save_notes()
            print("Note edited successfully.")
        else:
            print("Note not found.")

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note['id'] != note_id]
        self.save_notes()
        print("Note deleted successfully.")

def main():
    notes_app = NotesApp()

    while True:
        print("\n===== Notes App =====")
        print("1. Display Notes")
        print("2. Add Note")
        print("3. Read Note")
        print("4. Edit Note")
        print("5. Delete Note")
        print("0. Exit")

        choice = input("Enter your choice (0-5): ")

        if choice == '0':
            break
        elif choice == '1':
            notes_app.display_notes()
        elif choice == '2':
            title = input("Enter note title: ")
            body = input("Enter note body: ")
            notes_app.add_note(title, body)
        elif choice == '3':
            note_id = int(input("Enter note ID: "))
            notes_app.read_note(note_id)
        elif choice == '4':
            note_id = int(input("Enter note ID to edit: "))
            title = input("Enter new title: ")
            body = input("Enter new body: ")
            notes_app.edit_note(note_id, title, body)
        elif choice == '5':
            note_id = int(input("Enter note ID to delete: "))
            notes_app.delete_note(note_id)
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

if __name__ == "__main__":
    main()