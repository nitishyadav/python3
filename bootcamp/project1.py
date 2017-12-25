#making tic tac toe
'''
What needs to be done:
    We need to print a board 
    Take in player input
    Place their input on the board
    Check if the game is won, tied, lost or ongoing
    Repeat 3rd and 4th step until the game has been won or tied
    Ask if players want to play again
'''

'''
\Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
'''
from Ipython.display import clear_output
import random 

def display_board(board):
    pass

    
'''
Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.
'''
def player_input():
    pass

'''
Step 3: Write a function that takes, in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
'''
def place_marker(board, marker, position):
    pass

'''
Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. 
'''
def win_check(board, mark):
    pass

'''
Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.
'''
def choose_first():
    pass
    
'''
Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
'''
def space_check(board, position):
    pass

'''
Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
'''
def full_board_check(board):
    pass

'''
Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if its a free position. If it is, then return the position for later use. 
'''
def player_choice(board):
    pass

'''
Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
'''
def replay():
    pass

'''
Step 10:Use while loops and the functions you've made to run the game!
'''

print('welcome to Tic tac Toe!)

#while True:
    # Set the game up here
    #pass

    #while game_on:
        #Player 1 Turn
        
        
        # Player2's turn.
            
            #pass

    #if not replay():
        #break