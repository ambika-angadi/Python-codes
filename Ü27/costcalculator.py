#Display heading of cost calculator
print ("COST CALCULATOR")
print ("====================")

#Prompt user for the inputs
redwine_input = input ("How many red wines do you want to buy?:")
redwine = int(redwine_input)
redwine_price = redwine * 12.99

rosewein_input = input ("How many rosewein do you want to buy?:")
rosewein = int(rosewein_input)
rosewein_price = rosewein * 9.98

whitewine_input = input ("How many white wines do you want to buy?:")
whitewine = int(whitewine_input)
whitewine_price = whitewine * 11.99

#Calculate total price
total_price = redwine_price + rosewein_price + whitewine_price
print ("The total price of wines is: " + str(total_price))