mammal = "dog"
reptile = "crocodile, tortoise, snake"

enter_animal = input()

if enter_animal in mammal:
    print("mammal")
elif enter_animal in reptile:
    print("reptile")
else:
    print("unknown")
