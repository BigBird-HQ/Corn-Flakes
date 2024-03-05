from diary_app.Diary import Diary


class Diaries:
    def __init__(self):

        self.diaries = []

    def add(self, username, password):
        diary = Diary(username, password)
        self.diaries.append(diary)

    def get_number_of_diaries(self):
        return len(self.diaries)

    def find_by_username(self, username):
        for diary in self.diaries:
            if diary.get_username() == username:
                return diary

    def get_diaries(self):
        return self.diaries
