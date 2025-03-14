#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.
numbers_list = []

while True:
    user_input = int(input("Input a number: "))
    numbers_list.append(user_input)

    if numbers_list.count(user_input) == 1:
        print("Unique")
    else:
        print("Duplicate")