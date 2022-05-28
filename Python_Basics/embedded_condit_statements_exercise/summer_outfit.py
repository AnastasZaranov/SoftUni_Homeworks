from _ast import Break

degrees = int(input())  # e.g 30 degrees
time_of_day = input()  # Morning, Afternoon or Evening
outfit = ""
shoes = ""

if 10 <= degrees <= 18:
    if time_of_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif time_of_day == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif 18 <= degrees <= 24:
    if time_of_day == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_of_day == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif degrees >= 25:
    if time_of_day == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_of_day == "Afternoon":
        outfit = "Swimsuit"
        shoes = "Barefoot"
    elif time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
