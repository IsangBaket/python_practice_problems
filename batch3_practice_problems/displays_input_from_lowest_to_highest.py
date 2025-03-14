#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function
numbers_list = []

while True:
    user_input = int(input("Input a number: "))
    numbers_list.append(user_input)
    print("lowest number is: ", numbers_list.sort())