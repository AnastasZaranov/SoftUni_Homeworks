
while True:
    wizard = input()

    if wizard == "Voldemort":
        print("You must not speak of that name!")
        break
    elif wizard == "Welcome!":
        print("Welcome to Hogwarts.")
        break

    if len(wizard) < 5:
        print(f"{wizard} goes to Gryffindor.")
    elif len(wizard) == 5:
        print(f'{wizard} goes to Slytherin.')
    elif len(wizard) == 6:
        print(f'{wizard} goes to Ravenclaw.')
    elif len(wizard) > 6:
        print(f'{wizard} goes to Hufflepuff.')




