#Password Generator Project
#Mirza Mohammed Baig
#Dr.Angela Yu
#Python Project #5 from 100 Days of Code - The Complete Python Pro Bootcamp 
#June 6th, 2024

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to the PyPassword Generator!\n")

nr_letters = int(input("\nHow many letters would you like in your password?\n")) 

#for letters in range(1, nr_letters + 1):
#  random_letters += random.choice(letters)
  
nr_symbols = int(input(f"\nHow many symbols would you like?\n"))

#for symbols in range(1, nr_symbols + 1):
 # random_symbols += random.choice(symbols)

nr_numbers = int(input(f"\nHow many numbers would you like?\n"))

password_list = []

for char in range(1, nr_letters + 1):

  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

#Order of characters randomised:
randomized_password = ""
for char in password_list:
  randomized_password += char
print(f"\nYour password is: {randomized_password}")



