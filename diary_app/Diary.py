from diary_app.Entry import Entry
from diary_app.IncorrectPasswordError import IncorrectPasswordError


class Diary:
    def __init__(self, username, password):
        self.isLocked = False
        self.username = username
        self.password = password
        self.entries = []
        self.id_number = 1

    def is_locked(self):
        return self.isLocked

    def lock_diary(self):
        self.isLocked = True

    def unlock_diary(self, password):
        if self.password == password:
            self.isLocked = False
        else:
            raise IncorrectPasswordError('Incorrect Password')

    def create_entry(self, title, body):
        entry = Entry(self.id_number, title, body)
        self.id_number += 1
        self.entries.append(entry)

    def get_number_of_entry(self):
        return len(self.entries)

    def find_entry_by_id(self, id_number) -> Entry:
        for entry in self.entries:
            if entry.get_id() == id_number:
                return entry

    def delete_entry(self, id_number):
        entry = self.find_entry_by_id(id_number)
        self.entries.remove(entry)

    def update_entry(self, id_number, title, body):
        updated_entry = self.find_entry_by_id(id_number)
        updated_entry.set_body(body)
        updated_entry.set_title(title)

    def get_username(self):
        return self.username
