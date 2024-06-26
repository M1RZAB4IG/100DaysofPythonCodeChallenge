#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input(
    "What percentage tip would you like to give? 10, 12, or 15? "))
people_split = float(input("How many people to split the bill? "))


tip_percentage_float_final = (tip_percentage / 100) + 1
total_bill_float_final = total_bill * tip_percentage_float_final
total_bill_float_final_split = total_bill_float_final / people_split


print(f"Each person should pay: $ {total_bill_float_final_split:.2f}")

""""# Sample Input
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $124.56")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? 12")
people_split = input("How many people to split the bill? 7")

# Sample Output
Each person should pay: $19.93 """
