#import random module
import random

# Define a list of jokes
jokes = [
    "Hast du ein Bad genommen? Warum, fehlt eins?", "Egal, wie gut du schläfst: Albert schläft wie Einstein",
    "Wissenschaftler haben herausgefunden und sind wieder reingegangen.", "Sitzt einer im Stehcafé."
    "Wie heißt der Schutzpatron der Vergesslichen? Dings", "Hast du was zu trinken? Wasser. Nee, was Härteres! Ok, Eis."
    "Was ist rot und steht im Wald? Ein Kirsch", "Was ist weiß und rollt den Berg rauf? Eine Lawine mit Heimweh"
    "Wie nennt man einen Bumerang, der nicht zurückkommt? Stock", "Was ist das Gegenteil von Reformhaus? Reh hinterm Haus"
    "Wie nennt man ein Delfin in Unterhose? Slipper", "Egal wie voll du bist, Rudi war Völler."
]

#print a random joke from the list
joke = random.choice(jokes)
print (joke)

# Ask if the user wants one more joke
userchoice = input("One more joke? (y/n)")
if (userchoice == "y"):
    joke = random.choice(jokes)
    print (joke)
elif (userchoice == "n"):
    print ("bye for now")

#while True:
    # Choose a random joke from the list
    #joke = random.choice(jokes)
    
    # Output the joke to the console
    #print(joke)
    
    # Ask if the user wants another joke
    #response = input("One more joke? (y/n) ")
    #if response.lower() == "n":
        #break
