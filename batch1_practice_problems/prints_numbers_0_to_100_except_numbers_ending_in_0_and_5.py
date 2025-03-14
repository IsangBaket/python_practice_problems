#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
for number in range(101):
    if number %10 == 0:
        print('')
    if number %10 != 0:
        print(number)