#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
a = 0
for i in range(10):
    b = int(input("input a number: "))
    if b %2 == 0:
        a += 1

print(a)