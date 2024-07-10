# Take input from the user
input_string = input("Enter a comma-separated sequence of words: ")

# Split the input string into a list of words
words = input_string.split(',')

# Remove any leading or trailing whitespace from each word
words = [word.strip() for word in words]

# Convert the list to a set to remove duplicates, then convert back to a list
unique_words = list(set(words))

# Sort the list of unique words alphanumerically
unique_words.sort()

# Join the sorted list into a comma-separated string
result = ', '.join(unique_words)

# Print the result
print("Unique words in sorted order:", result)
