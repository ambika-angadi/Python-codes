#Display the heading of the time calculator
print ("TIME CALCULATOR")
print ("=======================")

#Prompt the user for input
user_input = input ("Enter the number of hours you want to convert:")
hour = int(user_input)
minutes = hour * 60
seconds = minutes * 60

print ("The number of hours are:" + str(hour))
print ("The " + str(hour) + " hour/s " + "has " + str(minutes) + " minutes and " + str(seconds) + " seconds.")



