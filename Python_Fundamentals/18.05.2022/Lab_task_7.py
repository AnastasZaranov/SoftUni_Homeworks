# Patterns

"""
Write a program that receives a number and creates the following pattern.
The number represents the largest count of stars on one row.

"""

num = int(input())

for i in range(1, num + 1):
    print(i*"*")

for j in range(num - 1, 0, -1):
    print(j*"*")


