# Mirza Mohammed Baig
# Dr.Angela Yu
# July 3rd, 2024
# 100DaysOfPythonChallenge = Day 10 

#Calculator 

from art import logo

#add
def add(n1, n2):
  return n1 + n2
#Subtract
def subtract(n1, n2):
  return n1 - n2
#Multiply
def multiply(n1, n2):
  return n1 * n2
#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}
def calculator(): 

  print(logo)
  num1 = float(input(f"What's the first number?: "))
  for symbol in operations:
    print(symbol)  
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input(f"What's the second number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
  
    print(f"The result is: {num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == "y":
      num1 = answer
    else:
      should_continue = False
      print()
      calculator()
    
calculator()
