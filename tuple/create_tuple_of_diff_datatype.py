# Creating a tuple with different data types
mixed_tuple = (1, 3.14, "apple", [1, 2, 3], {"key": "value"}, (4, 5, 6))
# Printing the tuple
print("Tuple with different data types:", mixed_tuple)
# Printing each element with its type
for element in mixed_tuple:
    print(f"Element: {element}, Type: {type(element)}")





#Second method using user input
user_input = input("Enter numbers separated by comma (,): ")
# Splitting the input string into individual elements and converting them to integers
numbers_list = [num for num in user_input.split(",")]
tup=tuple(numbers_list)
print(tup)
print(type(tup))