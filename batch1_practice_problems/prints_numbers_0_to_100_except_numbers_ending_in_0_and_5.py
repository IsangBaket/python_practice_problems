#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
for a in range(101):
    if a %10 == 0:
        print('')
    if a %10 != 0:
        print(a)