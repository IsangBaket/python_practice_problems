#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
numbers = []

for i in range(10):
    user_input = int(input("Input a number: "))
    numbers.append(user_input)  

result = numbers[0]  # First number as starting value

for num in numbers[1:]:  # Loop through remaining numbers
    result -= num 

print("Result:", result)
