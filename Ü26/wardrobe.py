# Create the wardrobe list
wardrobe = ["pants", "t-shirt", "dress"]

# Create the dresser list
dresser = ["shoes", "socks", "hats"]

# Output each item in the wardrobe individually
print (wardrobe[0])
print (wardrobe[1])
print (wardrobe[2])

# Display all the items in the wardrobe using a for loop
print("Items in the wardrobe:")
for item in wardrobe:
    print(item)

# Add a sweater to the wardrobe
wardrobe.append("sweater")

# Add the contents of the dresser to the wardrobe
wardrobe += dresser

# Display all the items added in the wardrobe
print("Updated items in the wardrbe:")
for item in wardrobe:
    print(item)
