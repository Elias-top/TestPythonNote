from datetime import datetime
import json
import os

from Note import Note


class Commands():
    def __init__(self, notes_file="notes.json"):
        self.notes_file = notes_file
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.notes_file):
            with open(self.notes_file, "r") as file:
                notes_data = json.load(file)
            notes = [Note(**data) for data in notes_data]
        else:
            notes = []
        return notes
    
    def save_notes(self):
        notes_data = [note.to_dict() for note in self.notes]
        with open(self.notes_file, "w") as file:
            json.dump(notes_data, file, indent=2)
    
    def addNote(self, title, body):
        note_id = len(self.notes) + 1
        time_creating = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        new_note = Note(note_id, title, body, time_creating)
        self.notes.append(new_note)

        self.save_notes()
        print(f"Заметка добавлена с ID = {note_id}")

    def readNotes(self):
        sorted_notes = sorted(self.notes, key=lambda x: datetime.strptime(x.dateCreate, "%Y-%m-%d %H:%M:%S"))
        if sorted_notes:
            for note in sorted_notes:
                print(f"ID: {note.id}\nЗаголовок: {note.title}\nТело: {note.body}\nДата/время: {note.dateCreate}\n")
        else:
            print("Заметок нет.")

    def readNote(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                print(f"ID: {note.id}\nЗаголовок: {note.title}\nТело: {note.body}\nДата/время: {note.dateCreate}\n")
                return
        print(f"Заметки с ID {note_id} не найдено.")

    def editNote(self, note_id, title, body):
        for note in self.notes:
            if note.id == note_id:
                note.title = title
                note.body = body
                note.dateCreate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                print(f"Заметка с ID {note_id} изменена.")
                return      
        print(f"Заметка с ID {note_id} не найдена.")

    def deleteNote(self, note_id):
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()
        print(f"Заметка с ID {note_id} удалена.")
    
    def showNotesByDate(self, target_date):
        target_date = datetime.strptime(target_date, "%Y-%m-%d").date()
        filtered_notes = [note for note in self.notes if datetime.strptime(note.dateCreate, "%Y-%m-%d %H:%M:%S").date() == target_date]
        for note in filtered_notes:
            print(f"ID: {note.id}\nЗаголовок: {note.title}\nТело: {note.body}\nДата/время: {note.dateCreate}\n")
