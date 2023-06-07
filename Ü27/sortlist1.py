#declare an empty list
unsorted_words = []

#Prompt the user to input list elements
while True:
    word_input = input("Enter a word to the list (q to quit): ")
    if (word_input != "q"):
        unsorted_words.append(word_input)
    elif (word_input == "q"): 
        break
print("unsorted list is: ", unsorted_words)

#Sort the unsorted list
sorted_words = sorted(unsorted_words, reverse=True )
print ("sorted list is:", sorted_words)
