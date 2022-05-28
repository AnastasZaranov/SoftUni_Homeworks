import sys

num_entry_amount = int(input())
min_val = sys.maxsize
max_val = -sys.maxsize

for i in range(num_entry_amount):
    n = int(input())
    if n < min_val:
        min_val = n
    if n > max_val:
        max_val = n

print(f'Max number: {max_val}\nMin number: {min_val}')