from commands import Commands


class MainMenu():
    commands_menu = Commands()
    inProgress = True
    def printMenu(self):
        print("Введите доступную команду из списка: ")
        print("1. Добавить заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Посмотреть список заметок")
        print("5. Вывести заметку по ID")
        print("6. Вывести заметку по Известной Дате")
        print("7. Выйти")

    def scanMenu(self):
        command = input("Введите номер операции: ")
        if(command == '1'):
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            self.commands_menu.addNote(title, body)
        elif(command == '2'):
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок: ")
            body = input("Введите новое тело заметки: ")
            self.commands_menu.editNote(note_id, title, body)
        elif(command == '3'):
            note_id = int(input("Введите ID заметки для удаления заметки: "))
            self.commands_menu.deleteNote(note_id)
        elif(command == '4'):
            self.commands_menu.readNotes()
        elif(command == '5'):
            note_id = int(input("Введите ID заметки для чтения заметки: "))
            self.commands_menu.readNote(note_id)
        elif(command == '6'):
            target_date = input("Введите дату в формате YYYY-MM-DD: ")
            self.commands_menu.showNotesByDate(target_date)
        elif(command == '7'):
            self.inProgress = False
        else:
            print("Недоступная команда")

    def start(self):
        while(self.inProgress):
            self.printMenu()
            self.scanMenu()
    
        