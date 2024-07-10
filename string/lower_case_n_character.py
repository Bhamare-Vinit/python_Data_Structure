def lowercase_first_n_chars(s, n):
    if n > len(s):
        n = len(s)
    return s[:n].lower() + s[n:]

# Sample string
sample_string = input("Enter the string :")
# Number of characters to lowercase
n = int(input("Enter value of n :"))

# Call the function with the sample string and n
result = lowercase_first_n_chars(sample_string, n)

# Print the result
print("Modified string:", result)
