from diary_app.Diary import Diary


class DiaryMainApp:
    def __init__(self):
        self.diary = Diary('username', 'password')

    def display(self):
        print('Welcome To Your Friendly Mavericks Diary')
        print('+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+')
        print('1. Create Entry\n2. Unlock\n3. Lock\n4. Check If Diary Is Locked\n5. Find\n6. Delete Entry\n7. '
              'Update\n8. Exit App')
        print('+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+')

        option = input('Select option: ')

        if option == '1':
            self.create_entry()
        elif option == '2':
            self.unlock()
        elif option == '3':
            self.lock()
        elif option == '4':
            self.check_if_diary_is_locked()
        elif option == '5':
            self.find_entry()
        elif option == '6':
            self.delete_entry()
        elif option == '7':
            self.update_entry()
        elif option == '8':
            self.exit()
        else:
            print('Enter a correct option from 1 to 8')
        self.display()

    def create_entry(self):
        title = input('Enter title: ')
        body = input('Write your thoughts here: ')
        self.diary.create_entry(title, body)
        print('\nEntry created successfully!\n\n')
        self.display()

    def unlock(self):
        password = input('Enter your password: ')
        if self.diary.password == password:
            self.diary.unlock_diary(password)
            print('Diary unlocked')
        else:
            print('Incorrect Password')
        self.display()

    def lock(self):
        password = input('Enter password: ')
        if self.diary.password == password:
            self.diary.lock_diary()
            print('Diary locked')
        else:
            print('Incorrect password')
        self.display()

    def check_if_diary_is_locked(self):
        password = input('Enter password: ')
        if self.diary.password == password:
            if self.diary.is_locked():
                print('Diary locked')
            else:
                print('Diary unlocked')
        else:
            print('Incorrect password')
        self.display()

    def find_entry(self):
        id_number = input('Enter ID')
        self.diary.find_entry_by_id(id_number)
        print('Entry found')
        self.display()

    def delete_entry(self):
        id_number = input('Enter ID')
        self.diary.delete_entry(id_number)
        print('Entry deleted successfully')

    def update_entry(self):
        id_number = input('Enter ID')
        title = input('Enter title: ')
        body = input('Write your thoughts here: ')
        self.diary.update_entry(id_number, title, body)
        print('Entry updated successfully')

    @staticmethod
    def exit():
        print('Exit')
        return


def main():
    diary_main_app = DiaryMainApp()
    diary_main_app.display()


if __name__ == "__main__":
    main()
