#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
a = []

for i in range(10):
    b = int(input("input a number: "))
    a.append(b)

c = a[0]
for b in a[1:]:
    c -= b

print(c)
