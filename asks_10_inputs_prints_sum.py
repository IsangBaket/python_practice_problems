#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
b = 0

for i in range(10):
    a = int(input("input a number: "))
    b += a

print(f"The sum of the ten numbers is {b}")