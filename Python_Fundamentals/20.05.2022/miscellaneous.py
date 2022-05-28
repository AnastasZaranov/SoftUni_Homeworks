number = "1234567"

# for current_digit in range(0, len(number)):
#    print(number[current_digit])
#    if number[current_digit] % 2 == 0:
#        print(number[current_digit])

for index, digit in enumerate(number):
    print(index, digit)

# enumerate() evokes the ability to show the index at which a variable is stored in an array.

some_string = "neprotivokonstitucionstvuvatelstvuvaite"
print(some_string[::-1])
# the above slicing method allows the string to be read backwards. The logic follows (start : end : step)

