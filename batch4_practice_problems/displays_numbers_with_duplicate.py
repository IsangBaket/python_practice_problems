#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
numbers_list = []

for _ in range(10):
    user_input = int(input("Input a number: "))
    numbers_list.append(user_input)

duplicates = {num for num in numbers_list if numbers_list.count(num) > 1}

print("Numbers with duplicates:", list(duplicates))
