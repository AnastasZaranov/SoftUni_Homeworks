
statement = True
new_string = ""

while statement is True:
    string = input()
    if string == "End":
        break
    if string == "SoftUni":
        continue
    else:
        for symbol in string:
            new_string += symbol * 2

    print(new_string)
    new_string = ""
