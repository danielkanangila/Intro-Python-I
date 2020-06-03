# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
    return "Even!" if num % 2 else "Odd"


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
print(is_even(num))
