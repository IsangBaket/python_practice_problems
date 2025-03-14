# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

#ask user to input numbers
#store input numbers in a variable
#compute average using addition and division
#automatically compute for average when user inputs
numbers = []

while True:
    user_input = int(input("Input a number: "))
    numbers.append(user_input)
    average = sum(numbers)/len(numbers)
    print(average)
