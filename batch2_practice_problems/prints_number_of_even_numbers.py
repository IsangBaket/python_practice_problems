#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
even_numbers_count = 0
for i in range(10):
    user_input = int(input("input a number: "))
    if user_input %2 == 0:
        even_numbers_count += 1

print(even_numbers_count)
