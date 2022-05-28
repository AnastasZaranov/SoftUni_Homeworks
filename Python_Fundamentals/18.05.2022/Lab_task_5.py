# Number Between 1 and 100

"""
Write a program that
Reads floating-point numbers from the console until it receives a number between 1 and 100 inclusive
When the correct number is received, stop reading and print "The number {number} is between 1 and 100"
"""

while True:
    num = float(input())
    if 1 <= num <= 100:
        print(f"The number {num} is between 1 and 100")
        break
