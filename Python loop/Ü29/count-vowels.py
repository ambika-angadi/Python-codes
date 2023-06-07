# Define the function to count the number of vowels
def count_vowels(x):
    vowels = "aeiouAEIOU"
    count = 0
    for char in x:
        if char in vowels:
            count += 1
    return count

# prompt the user for input
text = input("Enter some text: ")

# Count the vowels in the input and declare num_of_vowels variable
num_of_vowels = count_vowels(text)

# Print the result to the console
print(f"The number of vowels is {num_of_vowels}")

# Write the result to a file
with open("Number_Vowels.txt", "w") as f:
    f.write(f"The number of vowels in the input is {num_of_vowels}")
