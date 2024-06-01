# Mirza Mohammed Baig
# 100DaysofPythonChallenge: Day 4
# Dr.Angela Yu
# June 1st, 2024

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#create a list of the three variables
game_images = [rock, paper, scissors]


print("WELCOME TO ROCK, PAPER, SCISSORS!")

#get the user's choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

#check if the user's choice is valid 
if user_choice >= 3 or user_choice < 0: 
  #if the user's choice is not valid, print an error message
  print("You typed an invalid number, you lose!") 
else: 

    #print the image of the user's choice
    print(game_images[user_choice])

    #generate a random number between 0 and 2 to represent the computer's choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")

    #print the image of the computer's choice
    print(game_images[computer_choice])
    
    #compare the user's choice and the computer's choice to determine the winner
    if user_choice == 0 and computer_choice == 0:
        print("It's a draw!")
    elif user_choice == 1 and computer_choice == 0:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice == 0 and computer_choice == 1:
        print("You lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 1 and computer_choice == 1:
        print("It's a draw!")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose!")
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")
    elif user_choice == 2 and computer_choice == 2:
        print("It's a draw!")

  
    print("\nThanks for playing Rock, Paper, Scissors!")
    
