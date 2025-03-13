#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
a = []

for _ in range(10):
    c = int(input("Input a number: "))
    a.append(c)

for e in a:
    if a.count(e) == 1:
        print(e)


