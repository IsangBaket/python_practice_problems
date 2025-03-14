#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
numbers_list = []

for _ in range(10):
    user_input = int(input("Input a number: "))
    numbers_list.append(user_input)


numbers_with_duplicates = []

for num in numbers_list:
    if num not in numbers_with_duplicates:
        numbers_with_duplicates.append(num)
        
print(numbers_with_duplicates)