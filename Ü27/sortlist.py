#declare an empty list
unsorted_list = []

#Prompt the user to input list elements
while True:
    element_input = input("Enter an element  to the list (q to quit): ")
    if (element_input != "q"):
        value = int(element_input)
        unsorted_list.append(value)
    elif (element_input == "q"): 
        break
print("unsorted list is: ", unsorted_list)

#Sort the unsorted list
sorted_list = sorted(unsorted_list)
print ("sorted list is:", sorted_list)
