#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
numbers_list = []

for _ in range(10):
    user_input = int(input("Input a number: "))
    numbers_list.append(user_input)

numbers_with_no_duplicates = []

for num in numbers_list:
    if num in numbers_with_no_duplicates:
        numbers_with_no_duplicates.append(num) > 1
        
print(numbers_with_no_duplicates)
