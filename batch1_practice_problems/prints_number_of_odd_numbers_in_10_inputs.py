#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
odd_number_count = 0

for x in range(10):
    a = int(input("please input a number: "))
    if a %2 != 0:
        odd_number_count += 1

print(f"The total odd number is {odd_number_count}")
