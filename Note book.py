

class Note_Book:
    note_book = {
        "": ["", False, ""]
    }

    def __init__(self):
        self.qus = None
        self.note = None
        self.error = ["", " ", "  ", "   ", ",", "'"]
        self.error2 = ["", " ", "  ", "   "]

    def start_Game(self):
        n.print_option()
        self.qus = input("Enter your choice: ")
        if self.qus == "1":
            n.Take_Note()
        # elif self.qus == "2":
        #
        elif self.qus == "3":
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
        # elif self.qus == "4":
        #
        # elif self.qus == "5":
        #
        # elif self.qus == "6":

        elif self.qus == "7":
            print("Ok good bey!")
        else:
            print("Invalid input!")
            n.start_Game()

    def Take_Note(self):
        for note in self.note_book:
            self.note = input("Enter the name of the note you want to take: ")
            if self.note == self.note_book[self.note][2]:
                print("You already have this name in another note try again!")
                n.Take_Note()
            if self.note not in self.error:
                print(f"Ok the name of the Note is '{self.note}' Dont Forget it!")
                self.note_book[note] += self.note
                while True:
                    self.qus = input("Enter your Note in here: ")
                    if self.qus not in self.error2:
                        note += self.note
                        add_Note = f"{self.note}: {self.qus}"
                        self.note_book[self.note] = [self.qus, False, self.qus]
                        self.note_book[note][1] = True
                        print(f"=======>self.note = {self.note} note = {self.note_book[note]} self.qus = {self.qus} self.note_book = {self.note_book[note][0]}")
                        print("Ok your Note save successfully")
                        n.start_Game()
                    else:
                        print("Pls enter something!")
                        continue
            else:
                print("Pls enter something! and you can't use (')(,)")
                n.Take_Note()

    def print_option(self):
        print("1. Take a Note\n"
              "2. Delete a Note\n"
              "3. See all your Note\n"
              "4. Change Note\n"
              "5. See one Note\n"
              "6. Restart all\n"
              "7. Exit")


n = Note_Book()
n.start_Game()
