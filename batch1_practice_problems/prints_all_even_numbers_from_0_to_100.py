#Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)
for num in range(101):
    if num %2 == 0:
        print(num)
    if num %2 != 0:
        print('')