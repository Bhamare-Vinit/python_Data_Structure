
sample_dict = {
    'key1': [1, 2, 3],
    'key2': [],
    'key3': ['a', 'b', 'c', 'd'],
    'key4': [True, False]
}

for key, value in sample_dict.items():
    # Check if the value is a list
    if isinstance(value, list):
        count = len(value)
        # Print the result for each list
        print(f"Key '{key}' has {count} items: {value}")

    else:
        print(f"Key '{key}' does not have a list value.")

