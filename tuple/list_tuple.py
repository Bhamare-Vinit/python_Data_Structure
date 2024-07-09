# Taking user input
user_input = input("Enter numbers separated by spaces: ")

# Splitting the input string into individual elements and converting them to integers
numbers_list = [int(num) for num in user_input.split()]

tup=tuple(numbers_list)
print(f"The new created tuple is :\n{tup}")
print(f"Type of tuple is :{type(tup)}")