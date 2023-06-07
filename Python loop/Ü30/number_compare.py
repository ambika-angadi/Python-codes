#prompt the user for input
number1 = int(input("Please enter the 1st number: "))
number2 = int(input("Please enter the 2nd number: "))
number3 = int(input("Please enter the 3rd number: "))

#compare the numbers and output
if number1 > number2 and number1 > number3:
    print (f"{number1} is the biggest")
elif number2 > number1 and number2 > number3:
    print (f"{number2} is the biggest")
elif number3 > number1 and number3 > number1:
    print (f"{number3} is the biggest")
