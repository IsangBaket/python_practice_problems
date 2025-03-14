#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry
#start
#input 10 numbers
#python counts numbers
#python counts numbers with duplicates
#python stores first entry if numbers on one list variable
#python prints variable with stored first entry
#end

numbers_list = []

for _ in range(10):
    user_input = int(input("Input a number: "))
    numbers_list.append(user_input)

numbers_with_duplicates = []

for num in numbers_list:
    if num not in numbers_with_duplicates:
        numbers_with_duplicates.append(num)
        
print(num)