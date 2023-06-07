#define the function
def search(element, mylist):
    if element in mylist:
        print("True")
    else:
        print("False")

#prompt user for input
user_input = input("Please enter a list element: ")

#declare the list
mylist = ["chicken", "cow", "horse", "cat", "dog", "mouse"]

#call the function
search(user_input, mylist)


