#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
a = int(input("input a number: "))
b = int(input("input another number: "))

if a < b:
    print(a)
if b < a:
    print(b)