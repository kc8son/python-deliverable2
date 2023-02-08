####################################################################################################
#
#   Date Written: 02/07/2023        By: Joseph P. Merten
#   Grand Circus Unit 1
#   This script is part of the pre-work for the Grand Circus Data Analytics & Engineering bootcamp
#   Project 2: Fruit Market
#   Unit URL:
#       https://docs.google.com/document/d/12dPSSfFTqRJ9B5aPN8pdEcwMLq-wac4W0vhhRefIsdo/preview#heading=h.rtw57nbm41nk
#
#   Deliverable 2 Task
#   Write a program that allows the user to buy fruit. The program will display a list of different
#   fruits along with their prices. Keep asking the user if they'd like to purchase more fruit and
#   once they are done, print how many of each fruit they bought along with the subtotal and total
#   cost of their purchases.
#
####################################################################################################
#   imports
import math

####################################################################################################
#   Initialize our list of fruits: Fruit, Cost, Number bought, total spent, qualifier
fruit_list = [
    ["Apple", 2, 0, 0, "an"],
    ["Grape", 1, 0, 0, "a"],
    ["Orange", 3, 0, 0, "an"],
]

####################################################################################################
#   other variable initialization.
buy_fruit = "y"
purchase = 0
sub_total = 0
tax = 0
grand_total = 0

####################################################################################################
#   main code - start out getting the user's name..
print("Welcome to the GC Fruit Market!")
user_name = input("What is your name?\n")

####################################################################################################
#   Loop until no more purchases...
while buy_fruit.upper() == "Y":
    print(f"Welcome {user_name}. Which Fruit would you like to buy?")
    for i in range(3):
        print(f"{i+1}\t {fruit_list[i][0]}\t ${fruit_list[i][1]}")
    purchase = int(input())-1
    print(f"You bought {fruit_list[purchase][4]} {fruit_list[purchase][0]} at ${fruit_list[purchase][1]}")
    fruit_list[purchase][2] += fruit_list[purchase][1]
    fruit_list[purchase][3] += 1
    buy_fruit = input("Would you like to buy another piece of fruit? y / n?\n")

####################################################################################################
#   Print receipt...
# print(fruit_list)
print("Order for {user_name}")
for i in range(3):
    print(f"{fruit_list[i][3]} {fruit_list[i][0]}(s) at ${fruit_list[i][1]} a piece")
    sub_total += fruit_list[i][2]
tax = sub_total * .05
grand_total = tax + sub_total
print(f"Sub Total: ${sub_total}")
print(f"5% tax: ${tax}")
print(f"Total: ${grand_total}")


