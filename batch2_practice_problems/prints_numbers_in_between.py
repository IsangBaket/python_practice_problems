#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
num1 = int(input("input a number: "))
num2 = int(input("input another number: "))

for numbers in range(num1 + 1, num2):
    print(numbers)