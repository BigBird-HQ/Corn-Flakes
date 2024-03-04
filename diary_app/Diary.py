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
        id_number = self.generate_id(self)
        entry = Entry(id_number, title, body)
        self.entries.append(entry)

    @staticmethod
    def generate_id(self):
        return self.id_number

    def get_number_of_entry(self):
        return len(self.entries)

    def find_entry_by_id(self, id_number):
        for entry in self.entries:
            if entry.get_id() == id_number:
                return entry













