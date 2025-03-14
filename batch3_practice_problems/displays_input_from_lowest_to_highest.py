#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function
numbers_list = []

while True:
    try:
        user_input = int(input("Input a number: "))  
        numbers_list.append(user_input)
    except ValueError:  
        print("Invalid input. Exiting...\n")
        break

print("Numbers from lowest to highest:", sorted(numbers_list))