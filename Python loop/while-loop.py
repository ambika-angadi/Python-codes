#Syntax of while loop
#while condition:

count = 1

#die Schleife wird ausgeführt, solange count kleiner oder gleich als 5 ist
while count <= 5:
    print(count)
    count += 1 #erhöht count um 1 nach jeder Iteration

i = 1
n = 5

while i <= n:
    print(i)
    i = i + 1

#the loop is executed as long as the user doesn't input "ende"
while True:
    user_input = input("Geben Sie etwas ein (oder 'ende'):")
    if user_input == 'ende':
        break #the loop ends when the user inputs "ende"
    print("Sie haben " + user_input + " eingegeben")
