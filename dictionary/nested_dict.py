# Sample list
sample_list = ['a', 'b', 'c', 'd']

# Initialize the nested dictionary
nested_dict = current = {}

# Iterate over the list in reverse order to nest the keys
for key in sample_list:
    current[key] = {}
    current = current[key]

# Print the resulting nested dictionary
print(nested_dict)
