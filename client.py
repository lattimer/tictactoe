import pygame, sys, random
from pygame.locals import *
from tictactoe import Board

# Initialize pygame module
pygame.init()
pygame.display.list_modes()

# Init display window
disp = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Tic-Tac-Toe')

# RGB tuples
white = (255,255,255)
black = (0,0,0)
green = (64,255,32)
red = (255, 32,32)

# Mouse Offsets for tic tac toe squares
mo = [(100,100),(200,100),(300,100),(100,166),(200,166),(300,166),(100,233),(200,233),(300,233)]
player = "X"
comp = "O"
board = Board()

# Button offsets
quitButton = (215, 30, 70, 30)
resetButton = (115, 30, 70, 30)

fontObj = pygame.font.Font('freesansbold.ttf', 32)

# Helper method for displaying graphical text in Pygame
# str:  Display text
# fore: Foreground Color for text display
# back: Background Color for text display
# font: Pygame font object
# x:    Location on x-axis for text
# y:    Location on y-axis for text
def displayMessage(str, fore, back, font, x, y):
    textSurfaceObj = font.render(str, True, fore, back)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x, y)
    disp.blit(textSurfaceObj, textRectObj)

# Clear/reset game state
# No arguments
def initBoard():
    bfontObj = pygame.font.Font('freesansbold.ttf', 14)
    disp.fill(black)
    pygame.draw.line(disp, white, (300, 100), (300, 300), 4)
    pygame.draw.line(disp, white, (200, 100), (200, 300), 4)
    pygame.draw.line(disp, white, (100, 166), (400, 166), 4)
    pygame.draw.line(disp, white, (100, 233), (400, 233), 4)
    pygame.draw.rect(disp, white, resetButton)
    pygame.draw.rect(disp, white, quitButton)
    displayMessage("Reset", black, white, bfontObj, 150, 45)
    displayMessage("Quit", black, white, bfontObj, 250, 45)

initBoard()

# Main game loop
while True: 


    for event in pygame.event.get():
        # OS level quit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        # Mouse event handler
        if event.type == MOUSEBUTTONDOWN:
            pos = event.pos

            # Reset button handler
            if pos[0] > resetButton[0] and pos[0] < (resetButton[0] + resetButton[2]) and pos[1] > resetButton[1] and pos[1] < (resetButton[1] + resetButton[3]):
                board.__init__()
                initBoard()
            # Quit button handler
            if pos[0] > quitButton[0] and pos[0] < (quitButton[0] + quitButton[2]) and pos[1] > quitButton[1] and pos[1] < (quitButton[1] + quitButton[3]):
                pygame.quit()
                sys.exit()

            # Create 9 mouse handlers for handling different possible plays in tic tac toe

            for i in range(len(mo)) :

                if pos[0] > mo[i][0] and pos[0] < mo[i][0]+100 and pos[1] > mo[i][1] and pos[1] < mo[i][1]+66:
                    # Input validation
                    if (board.gs[i] == " "):
                        # Draw the X
                        pygame.draw.line(
                            disp, green, (mo[i][0] + 25, mo[i][1] + 15), (mo[i][0] + 75, mo[i][1] + 55), 6)
                        pygame.draw.line(
                            disp, green, (mo[i][0] + 25, mo[i][1] + 55), (mo[i][0] + 75, mo[i][1] + 15), 6)
                        board.inputMove(i, player)

                        # Check for win condition
                        if board.checkForWinner(player):
                            displayMessage("You win!!", green, black,
                                           fontObj, 200, 340)
                        # Check for draw so we can skip computers turn
                        elif board.checkForDraw():
                            displayMessage("Looks like a cats game!!", white, black,
                                           fontObj, 250, 340)
                        elif (board.playAgain == " "):
                        
                            cmove = board.moveAI(comp, player)
                            board.inputMove(cmove, comp)
                            # Draw the O
                            pygame.draw.circle(
                                disp, red, (mo[cmove][0] + 50, mo[cmove][1] + 35), 25, 6)

                            if board.checkForWinner(comp):
                                displayMessage("You lose!!", red, black,
                                               fontObj, 200, 340)
        
        # Only need to update the display on a mouse press                                               
        pygame.display.update()


