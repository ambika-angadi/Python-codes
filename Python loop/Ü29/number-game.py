import random

# declare number variable that holds random number generated
number = random.randint(0, 9)

# initialize the number of guesses
no_of_guesses = 0

# loop until the user guesses the number
while True:
    guess = int(input("Please enter a number: "))
    no_of_guesses += 1

    if guess < number:
        print("The number is too low")
    elif guess > number:
        print("The number is too high")
    else:
        print(f"Correct! You guessed the number in {no_of_guesses} attempts.")
        break
