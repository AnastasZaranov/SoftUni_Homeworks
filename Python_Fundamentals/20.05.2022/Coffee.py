coffees = 0
uppers = "CAT, DOG, MOVIE, CODING"
lowers = "cat, dog, movie, coding"

while True:
    statement = input()

    if statement in uppers:
        coffees += 2
    elif statement in lowers:
        coffees += 1
    else:
        pass

    if statement == "END":
        break

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)