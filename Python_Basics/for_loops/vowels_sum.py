text = input()
calc = 0
a = 1
e = 2
i = 3
o = 4
u = 5

for x in range(0, len(text)):
    if text[x] == "a":
        calc += a
    elif text[x] == "e":
        calc += e
    elif text[x] == "i":
        calc += i
    elif text[x] == "o":
        calc += o
    elif text[x] == "u":
        calc += u
print(calc)
