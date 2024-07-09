# Taking user input
user_input = input("Enter numbers separated by spaces: ")

# Splitting the input string into individual elements and converting them to integers
numbers_list = [int(num) for num in user_input.split()]

# Initializing the product variable to 1 (multiplicative identity)
product = 1

# Multiplying all items in the list
for num in numbers_list:
    product *= num

# Printing the result
print("The product of all items in the list is:", product)