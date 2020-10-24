class TicTacToe:
    def __init__(self, player1, player2):
        # Players
        self.player1 = player1
        self.player2 = player2

        # Board
        self.playboard = [['_', '_', '_'],
                          ['_', '_', '_'],
                          ['_', '_', '_']]

        # Board Coordinates
        self.COORDS = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2]
        }

        # Symbols
        self.SYMBOLS = ['X', 'O']

    def user_input(self, player):
        """
        This function acts as gateway for user decisions 
        :param player: Player info
        :return: Redirects to other functions
        """
        print("Choose your choice!")
        print("1: Display board\n"
              "2: insert symbol")
        user = input("Enter your choice: ")
        if user.isdigit():
            if int(user) == 1:
                self.display()
                print("***insert A SYMBOL***")
                c = int(input("Enter area to insert symbol: "))
                return self._insert(c, player[1])
            elif int(user) == 2:
                c = int(input("Enter area to insert symbol: "))
                return self._insert(c, player[1])
            else:
                print("INVALID INPUT!!")
        else:
            print("INVALID INPUT!!")

    def display(self):
        """
        Displays the current board status
        :return:  NULL
        """
        for i in self.playboard:
            print(" ".join(i))
        print("")

    def _choice(self, area):
        """
        This function acts as a gateway for player's choice.
        :param area: int between 1 - 9 which represents the areas on the board
        :return: coordinates of the area
        """
        return self.COORDS.get(area)

    def _insert(self, c, symbol):
        """
        This function inserts player's symbol into the board
        :param c: Player's choice
        :param symbol: Player's symbol
        :return: Updated board
        """
        choice = self._choice(c)
        x, y = choice[0], choice[1]
        if self.playboard[x][y] in self.SYMBOLS:
            print("***AREA ALREADY OCCUPIED***")
            c = int(input("Enter area to insert symbol: "))
            return self._insert(c, symbol)
        else:
            self.playboard[x][y] = symbol
            print("***AREA UPDATED***")
        return self.playboard

    def validate_board(self):
        """
        This function validates the board
        :return: Boolean value of whether the game is over or not
        """
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
        """
        Creates a player
        :return: Player's info
        """
        name = input("Enter your name: ").title()
        symbol = input("Enter your symbol: ").upper()

        while symbol not in ['X', 'O']:
            print("INVALID SYMBOL!!")
            symbol = input("Enter your symbol: ").upper()

        return name, symbol
