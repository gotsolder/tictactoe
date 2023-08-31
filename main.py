import re

# https://patorjk.com/software/taag/#p=testall&f=Blocks&t=Tic
logo = """
  _____ _        _____            _____          
 |_   _(_) ___  |_   _|_ _  ___  |_   _|__   ___
   | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / __/
   | | | | (__    | | (_| | (__    | | (_) |  __/
   |_| |_|\___|   |_|\__,_|\___|   |_|\___/ \___|                                                 
"""

intro_help = '''
When you choose a position, select a number from 1..9:

   1  !  2  |  3
 -----+-----+-----
   4  !  5  |  6
 -----+-----+-----
   7  !  8  |  9
'''


ways_to_win = ['123', '456', '789', '147', '258', '369', '159', '357']


class TicTacToe:
    def __init__(self):
        self.board = [f'{x}' for x in range(1, 10)]
        self.turns_left = 9
        self.draws = 0
        player1.pos_list = []
        player2.pos_list = []

    def print(self):
        board = [x if re.match("[XO]", x) else " " for x in self.board]

        print(f"\n   {board[0]}  |  {board[1]}  |  {board[2]}")
        print(" -----+-----+-----")
        print(f"   {board[3]}  |  {board[4]}  |  {board[5]}")
        print(" -----+-----+-----")
        print(f"   {board[6]}  |  {board[7]}  |  {board[8]}\n")


class Player:
    def __init__(self, xo):
        self.xo = xo
        self.name = input(f"Who is gonna be the {self.xo}'s: ").strip().title()
        self.wins = 0
        self.pos_list = []

    def is_winner(self):
        for three_some in ways_to_win:
            if three_some[0] in self.pos_list and \
               three_some[1] in self.pos_list and \
               three_some[2] in self.pos_list:
                return True
        return False

    def take_turn(self):
        if game.turns_left == 0:
            print("IT's A DRAW !!!")
            game.draws += 1
            return True

        while True:
            pos = input(f"{self.name}, Enter a position for your '{self.xo}' (1-9): ")
            if not re.match("^[1-9]$", pos):
                print(f"Whoops, '{pos}' is not a valid position!  Try again.")
            elif pos not in game.board:
                print(f"Whoops, position {pos} is already taken!  Try again.")
            else:
                game.turns_left -= 1
                self.pos_list.append(pos)
                game.board[int(pos) - 1] = self.xo
                game.print()
                if self.is_winner():
                    print(f"{self.name} WON!!\n")
                    self.wins += 1
                    return True
                return False


print(logo)
print(intro_help)

player1 = Player('X')
player2 = Player('O')

new_game = True

while True:
    if new_game:
        new_game = False
        game = TicTacToe()
        game.print()

    if player1.take_turn() or player2.take_turn():
        # somebody won or there was a draw
        print(f"Score: {player1.name}: {player1.wins}     {player2.name}: {player2.wins}     Draws: {game.draws}\n")
        new_game = True
        if input("Do you want to play again (y|n)?: ").strip().upper()[0] == "N":
            print("Goodbye...")
            exit(0)
