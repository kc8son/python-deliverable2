####################################################################################################
#
#   Date Written: 02/06/2023        By: Joseph P. Merten
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
#   Initialize our list of fruits: Fruit, Cost, Number bought
fruit_list = [
    ["Apple", 2, 0],
    ["Grape", 1, 0],
    ["Orange", 3, 0],
]

####################################################################################################
#   main code - start out getting the user's name..
print("Welcome to the GC Fruit Market!")
user_name = input("What is your name?\n")