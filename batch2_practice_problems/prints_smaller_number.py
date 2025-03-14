#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
num1 = int(input("input a number: "))
num2 = int(input("input another number: "))

if num1 < num2:
    print(num1)
if num2 < num1:
    print(num2)