sample_dict = {
    'maths': 99,
    'science': 97,
    'sanskrit': 99,
    'english': 89,
    'civics': 95,
    'marathi': 79,
}

# Iterate over the keys of the dictionary
print("Iterating over keys:")
for key in sample_dict:
    print(key)

print("\nIterating over key-value pairs:")
# Iterate over the key-value pairs of the dictionary
for key, value in sample_dict.items():
    print(f"{key}: {value}")

print("\nIterating over values:")
# Iterate over the values of the dictionary
for value in sample_dict.values():
    print(value)

print("\nIterating over keys and accessing values:")
# Iterate over the keys and access values
for key in sample_dict.keys():
    print(f"{key}: {sample_dict[key]}")