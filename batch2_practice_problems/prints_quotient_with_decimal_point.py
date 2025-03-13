#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point
a = int(input("input a number: "))
b = int(input("input another number: "))
c = a/b 

print(f"{c:.0f}")