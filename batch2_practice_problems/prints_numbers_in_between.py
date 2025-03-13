#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
a = int(input("input a number: "))
b = int(input("input another number: "))

for i in range(a + 1, b):
    print(i)