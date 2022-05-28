# Shopping
"""
Write a program that
Reads a budget and then prices of each product you need to buy until it receives the command "End"
If there is not enough budget left for the next product, prints "You went in overdraft!" and end the program
If you bought everything needed and the program receives "End", prints "You bought everything needed."
"""

money = input()
budget = int(money)

while True:
    entry = input()
    if entry == "End":
        print("You bought everything needed")
        break



