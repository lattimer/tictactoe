import random

# Object for managing the state and functionality of a tic tac toe game
class Board:

    def __init__(self):
        self.gs = [" "] * 9       # Game state
        self.playAgain = " "      # Manage main game loop

    # Display board in console
    def refreshBoard(self):
        repLine = "─┼─┼─"
        for i in range(0,7,3):
            print(self.gs[i]+"|"+self.gs[i+1]+"|"+self.gs[i+2]);
            if i != 6:
                print (repLine)

    # Alter game state
    def inputMove(self, move, player):
        self.gs[move] = player
        

    # Check if player has reached 1 of 8 win conditions in tic tac toe
    def checkForWinner(self, player):
        pat = player*3
        return ("".join(self.gs[0:3]) == pat or "".join(self.gs[3:6]) == pat
        or "".join(self.gs[7:9]) == pat or "".join(self.gs[0:7:3]) == pat
        or "".join(self.gs[1:8:3]) == pat or "".join(self.gs[2:9:3]) == pat
        or "".join(self.gs[0:9:4]) == pat or "".join(self.gs[2:7:2]) == pat)

    # Decision tree to determine optimal move, returns the best move for computer
    def moveAI(self, player):
        corners = [0,2,6,8]
        cardinal = range(1,8,2)
        moves = []
        
        # See if computer can win
        for i in range(0,9):
            if self.gs[i] == " ":
                self.gs[i] = player
                if self.checkForWinner(player):
                    return i
                else: 
                    self.gs[i] = " "
        # Make a move to one of the corners randomly if no winning move is found
        for i in corners:
            if self.gs[i] == " ":
                moves.append(i)
        if len(moves) != 0:
            return random.choice(moves)
        # Make a move to the center
        if self.gs[4] == " ":
            return 4
        # Otherwise, make a move to one of the cardinal directions
        for i in cardinal:
            if self.gs[i] == " ":
                moves.append(i)
        if len(moves) != 0:
            return random.choice(moves)

    def checkForDraw(self):
        if " " not in self.gs:
            print ("Looks like a cats game pal!")
            self.playAgain = input("Would you like to play again? ").lower()[0:1]

    def endGame(self, player):
        self.refreshBoard()
        print("{} woN!".format(player))
        self.playAgain = input("Would you like to play again? ").lower()[0:1]

# Make new tictactoe board object

board = Board()

# Main game loop

while (board.playAgain != "n"):
    
    player = "X"
    comp = "O"
    
    board.refreshBoard()
    move = int(input("\nPlease input your move: "))
    
    
    # Input validation
    while move <= -1 or move >= 9 or board.gs[move] != " ":
        print("Invalid move!")
        move = int(input("\nPlease input your move: "))    
    
    # Player turn
    board.inputMove(move, player)    

    if board.checkForWinner(player):
        board.endGame(player)

    board.checkForDraw()
    
    # If game is getting restarted, skip computer turn to proceed with new loop
    if (board.playAgain == " "):
        # Computer turn
        cmove = board.moveAI(comp)
        board.inputMove(cmove, comp)
        
        if board.checkForWinner(comp):
            board.endGame(comp)
        
    if board.playAgain == "y":
        board.__init__()
    
