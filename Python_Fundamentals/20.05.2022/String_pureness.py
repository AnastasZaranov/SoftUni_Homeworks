"""
You will be given number n. After that, you'll receive different strings n times.
Your task is to check if the given strings are pure, meaning that they do NOT consist of any of the characters:
comma ",", period ".", or underscore "_":

•	If a string is pure, print "{string} is pure."
•	Otherwise, print "{string} is not pure!"

"""

n = int(input())

for i in range(n):
    string = str(input())
    if "," in string or "." in string or "_" in string:
        print(f'{string} is not pure!')
    else:
        print(f'{string} is pure.')
