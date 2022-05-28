"""
On the first line, you will be given a positive number, which will serve as a divisor.

On the second line, you will receive a positive number that will be the boundary.

You should find the largest integer N, that is:

· divisible by the given divisor

· less than or equal to the given bound

· greater than 0

Note: it is guaranteed that N is found.
"""

d = int(input())
b = int(input())
c = b - 1
e = b - (b % d)

if b % d == 0:
    print(b)
elif c % d == 0:
    print(c)
else:
    print(e)
