# Even Numbers
# Write a program that
# Receives a number n and then receives n different numbers
# If it receives an odd number, print "{num} is odd!" and end the program
# If all numbers are even print "All numbers are even#

n = int(input())
count = 0

for i in range(n):
    new = int(input())
    count += 1
    if new % 2 != 0:
        print(f'{new} is odd!')
        break
    elif count == n:
        print("All numbers are even.")
        break
    else:
        continue

