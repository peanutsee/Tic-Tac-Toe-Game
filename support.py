class TicTacToe:
    def __init__(self, player1, player2):
        # Players
        self.player1 = player1
        self.player2 = player2

        # Board
        self.playboard = [['_', '_', '_'],
                          ['_', '_', '_'],
                          ['_', '_', '_']]

        self.SYMBOLS = ['X', 'O']

        self.COORDS = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2]
        }

    def user_input(self, player):
        print("Choose your choice!")
        print("1: Display board\n"
              "2: Insert symbol")
        user = input("Enter your choice: ")
        if user.isdigit():
            if int(user) == 1:
                self.display()
                print("***INSERT A SYMBOL***")
                c = int(input("Enter area to insert symbol: "))
                return self.insert(c, player[1])
            elif int(user) == 2:
                c = int(input("Enter area to insert symbol: "))
                return self.insert(c, player[1])
            else:
                print("INVALID INPUT!!")
        else:
            print("INVALID INPUT!!")

    def display(self):
        for i in self.playboard:
            print(" ".join(i))
        print("")

    def choice(self, symbol):
        return self.COORDS.get(symbol)

    def insert(self, c, symbol):
        choice = self.choice(c)
        x, y = choice[0], choice[1]
        if self.playboard[x][y] in self.SYMBOLS:
            print("***AREA ALREADY OCCUPIED***")
            c = int(input("Enter area to insert symbol: "))
            return self.insert(c, symbol)
        else:
            self.playboard[x][y] = symbol
            print("***AREA UPDATED***")
        return self.playboard

    def validate_board(self):
        # Check Rows
        for row in range(3):
            if len(set(self.playboard[row])) == 1 and "_" not in self.playboard[row]:
                return False

        # Check Columns
        cols = []
        for col in range(3):
            column = []
            for row in range(3):
                column.append(self.playboard[row][col])
            cols.append(column)

        for col in range(3):
            if len(set(cols[col])) == 1 and "_" not in cols[col]:
                return False

        # Check Diagonals
        diagonals = [[self.playboard[i][i] for i in range(3)]]

        right_diag = []
        j = 2
        for i in range(3):
            right_diag.append(self.playboard[i][j])
            j -= 1
        diagonals.append(right_diag)

        for diag in diagonals:
            if len(set(diag)) == 1 and "_" not in diag:
                return False

        return True


class Player:
    @staticmethod
    def create_player():
        name = input("Enter your name: ")
        symbol = input("Enter your symbol: ").upper()

        while symbol not in ['X', 'O']:
            print("INVALID SYMBOL!!")
            symbol = input("Enter your symbol: ").upper()

        return name, symbol
