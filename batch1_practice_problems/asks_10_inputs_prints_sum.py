#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
sum = 0

for number in range(10):
    user_input = int(input("input a number: "))
    sum += user_input

print(f"The sum of the ten numbers is {sum}")