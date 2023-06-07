#Prompt user for input
number = int(input("Please input a positive integer:"))
factorial = 1
for i in range(1, number+1):
    factorial = factorial * i
print(" The factorial of ", number, " is", factorial)
