#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
numbers_list = []

for _ in range(10):
    user_input = int(input("Input a number: "))
    numbers_list.append(user_input)

for no_duplicate in numbers_list:
    if numbers_list.count(no_duplicate) == 1:
        print(no_duplicate)


