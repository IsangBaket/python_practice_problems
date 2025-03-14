#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
numbers_list = []

while True:
    user_input = int(input("Input a number: "))
    numbers_list.append(user_input)
    print(min(numbers_list))