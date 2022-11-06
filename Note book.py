

class Note_Book:
    note_book = {
        "": ["", False, "", ""],
        " ": ["", False, "", ""]
    }

    def __init__(self):
        self.qus = None
        self.note = None
        self.error = ["", " ", "  ", "   ", ",", "'"]
        self.error2 = ["", " ", "  ", "   "]
        self.save = ""

    def start_Game(self):
        n.print_option()
        self.qus = input("Enter your choice: ")
        if self.qus == "1":
            n.Take_Note()
        elif self.qus == "2":
            n.delete_Note()
        elif self.qus == "3":
            n.see_all_Note()
        elif self.qus == "4":
            n.change_note()
        elif self.qus == "5":
            n.see_one_Note()
        elif self.qus == "6":
            n.restart_all()
        elif self.qus == "7":
            n.see_all_name_note()
        elif self.qus == "8":
            print("Ok good bey!")
            exit()
        else:
            print("Invalid input!")
            n.start_Game()

    def Take_Note(self):
        for note in self.note_book:
            self.note = input("Enter the name of the note you want to take: ")
            key = self.note
            val = self.note_book.get(key)
            if val is not None:
                print(f"You pick an invalid option or You already have this name in another note try again!")
                n.Take_Note()
            else:
                self.save = self.note
                if self.note not in self.error:
                    print(f"Ok the name of the Note is '{key}' Dont Forget it!")
                    self.note_book[note] += key
                    while True:
                        self.qus = input("Enter your Note in here: ")
                        if self.qus not in self.error2:
                            note += key
                            add_Note = f"{key}: {self.qus}"
                            self.note_book[key] = [self.qus, False, self.qus, self.save]
                            self.note_book[note][1] = True
                            print("Ok your Note save successfully")
                            n.start_Game()
                        else:
                            print("Pls enter something!")
                            continue

    def see_all_Note(self):
        my_string = "\n"
        for key in self.note_book:
            if self.note_book[key][1]:
                my_string += f"{self.note_book[key][0]}\n"

        if my_string == "\n":
            print("You dont have any Note yet!")
        else:
            print(f"Ok your Note are: {my_string}")
        input("press enter to go back: ")
        n.start_Game()

    def delete_Note(self):
        self.qus = input("Enter the name of the note if you dont remember press (c) to go back if you remember enter it here: ")
        if self.qus == "c":
            n.start_Game()
        else:
            pass
        key = self.qus
        val = self.note_book.get(key)
        if val is None:
            print(f"You pick an invalid option try again!")
            n.delete_Note()
        else:
            if self.note_book[key][2] == "":
                print("Pls enter the name next time!")
                n.delete_Note()
            else:
                print("The Note Deleted! successfully!!")
                del self.note_book[key]
                n.start_Game()

    def change_note(self):
        self.qus = input("Enter the name of the note if you dont remember press (c) to go back if you remember enter it here: ")
        if self.qus == "c":
            n.start_Game()
        else:
            pass
        key = self.qus
        val = self.note_book.get(key)
        if val is None:
            print(f"You pick an invalid option try again!")
            n.change_note()
        else:
            if self.note_book[key][2] == "":
                print("Pls enter the name next time!")
                n.change_note()
            else:
                for note in self.note_book:
                    while True:
                        self.qus = input("Enter your New Note: ")
                        key1 = self.qus
                        val = self.note_book.get(key1)
                        if val is None:
                            self.note_book[key][0] = key1
                            self.note_book[key][2] = key1
                            print("The Note Change! successfully!!")
                            n.start_Game()
                        else:
                            print("Pls enter something in your note!")
                            continue

    def see_one_Note(self):
        self.qus = input(
            "Enter the name of the note if you dont remember press (c) to go back if you remember enter it here: ")
        if self.qus == "c":
            n.start_Game()
        else:
            pass
        key = self.qus
        val = self.note_book.get(key)
        if val is None:
            print(f"You pick an invalid option try again!")
            n.delete_Note()
        else:
            if self.note_book[key][2] == "":
                print("Pls enter the name next time!")
                n.delete_Note()
            else:
                print(f"OK the note in this name is:\n{self.note_book[key][0]}")
                n.start_Game()

    def restart_all(self):
        for item in self.note_book:
            self.note_book = {
                "": ["", False, "", ""],
                " ": ["", False, "", ""]
            }
            print("The restart complete!")
            n.start_Game()

    def see_all_name_note(self):
        print(f"=============={self.save}")
        my_string = "\n"
        for key in self.note_book:
            if self.note_book[key][3] not in self.error2:
                my_string += f"{self.note_book[key][3]}\n"

        if my_string == "\n":
            print("You dont have any Note name yet!")
        else:
            print(f"Ok your Note name are: {my_string}")
        input("press enter to go back: ")
        n.start_Game()

    def print_option(self):
        print("1. Take a Note\n"
              "2. Delete a Note\n"
              "3. See all your Note\n"
              "4. Change Note\n"
              "5. See a specific Note\n"
              "6. Restart all\n"
              "7. See all of the name of the Note\n"
              "8. Exit")


n = Note_Book()
n.start_Game()
