#Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.
print("THIS PROGRAM WILL PRINT THE VALUE OF A NUMBER WHEN RAISED TO THE SECOND NUMBER")
base = float(input("Input a base number: "))
exponent = float(input("Input exponent number: "))

result = base**exponent

print(f"{base} raised to {exponent} is {result}")
