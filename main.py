import random


class bomb_avoid:
    board_ = {
        1: ["0", "#", 1, False],
        2: ["0", "#", 2, False],
        3: ["0", "#", 3, False],
        4: ["0", "#", 4, False],
        5: ["0", "#", 5, False],
        6: ["0", "#", 6, False],
        7: ["0", "#", 7, False],
        8: ["0", "#", 8, False],
        9: ["0", "#", 9, False],
    }

    def __init__(self):
        self.All = None
        self.qus = None
        self.num = 0

        self.All = [self.board_[1][1], self.board_[2][1], self.board_[3][1], self.board_[9][1], self.board_[5][1],
                    self.board_[6][1], self.board_[7][1], self.board_[8][1], self.board_[4][1]]

        self.ran = random.randint(0, 8)

        random.shuffle(self.All)

    def start_game(self):
        b.board()
        self.qus = input("Where you want to put your pick (1,9): ")
        key = self.qus
        if key.isdigit():
            key = int(key)
        else:
            print("You enter an invalid input try again!")
            b.start_game()
        if self.num == 8:
            print("congruent you won!")
            b.restart()

        if key == self.board_[key][2] and self.board_[key][3] is False:
            if key - 1 == self.ran:
                print("You pick the bomb you blow up and lost!")
                self.All[key - 1] = "*"
                b.board()
                b.restart()
            else:
                pass

            self.All[key - 1] = self.board_[key][0]
            self.board_[key][3] = True
            self.num += 1

            b.start_game()
        else:
            print("You pick this place already pick, pick other place!")
            b.start_game()

    def board(self):
        print(f"{self.All[0]}, {self.All[1]}, {self.All[2]}\n"
              f"{self.All[3]}, {self.All[4]}, {self.All[5]}\n"
              f"{self.All[6]}, {self.All[7]}, {self.All[8]}")

    def restart(self):
        self.qus = input("You want to try again? (y/n): ")
        if self.qus == "y":
            random.shuffle(self.All)
            self.num = 0
            b.start_game()
        else:
            print("Ok good bey")
            exit()


b = bomb_avoid()
b.start_game()
