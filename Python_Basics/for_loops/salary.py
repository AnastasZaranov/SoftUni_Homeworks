open_tabs = int(input())
salary = int(input())


for tab in range(0, open_tabs):
    website = input()
    if website == "Facebook":
        salary -= 150
        if salary <= 0:
            print("You have lost your salary.")
            break
    elif website == "Instagram":
        salary -= 100
        if salary <= 0:
            print("You have lost your salary.")
            break
    elif website == "Reddit":
        salary -= 50
        if salary <= 0:
            print("You have lost your salary.")
            break
if salary != 0:
    print(f'{salary}')
