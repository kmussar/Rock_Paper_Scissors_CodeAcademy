"""This program plays rock, paper, scissors. 
The steps are: 
    1. Prompt the user to select either Rock, Paper, or Scissors. 
    2. Instruct the computer to randomly select either Rock, Paper, or Scissors. 
    3. Compare the user's choice and the computer's choice 
    4. Determine a winner (the user or the computer) 
    5. Inform the user who the winner is""" 
# Import the neccessary functions
from random import randint  
from time import sleep 

# Set static variables
options = ["R", "P", "S"]
LOST = "Sorry, you lost this time."
WIN = "You win!"

""" this function asks for the user's choice, 
 chooses R/P/S for the computer, compares the values, and
 returns who the winner is. """
def decide_winner(user_choice, computer_choice):
  print("You selected %s." % user_choice)
  print("Computer selecting...")
  sleep(1)
  print("Computer selected %s." % computer_choice)
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  if user_choice_index == computer_choice_index: 
    print("You tie!")
  elif user_choice_index == 0 and computer_choice_index == 2:
    print(WIN)
  elif user_choice_index == 1 and computer_choice_index == 0:
    print(WIN) 
  elif user_choice_index == 2 and computer_choice_index == 1:
    print(WIN)
  elif user_choice_index > 2: 
    "You have selected an invalid option."
    return 
  else: 
    print(LOST)

"""This function defines the operations of the game. """
def play_RPS(): 
  print("Rock, paper, scissors?")
  user_choice = input("Select R for Rock, P for Paper, or S for Scissors:").upper()
  sleep(1)
  computer_choice = options[randint(0,len(options)-1)]
  decide_winner(user_choice,computer_choice)

# this command runs the game
play_RPS()