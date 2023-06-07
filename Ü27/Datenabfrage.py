#Display the heading
print ("DATENABFRAGE")
print ("=================")

#Prompt the user for input
print ("Please enter the following details")

#Store the user input into a variable
surname = input("Surname: ")
firstname = input("First name: ")
age = input("Age: ")
plz = input("PLZ: ")
place = input("Place: ")

#Output all the details
print (firstname + " " + surname + " is " + age + " years old and lives in " + plz + " " + place + "." )