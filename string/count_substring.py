def count_substring(main_string, sub_string):
    # Use the count method of the string to count occurrences of the substring
    return main_string.count(sub_string)

# Sample string
main_string = input("Enter the string :")
# Substring to count
sub_string = input("Enter the sub-string :")

# Call the function with the sample string and substring
count = count_substring(main_string, sub_string)

# Print the result
print(f"The substring '{sub_string}' occurs {count} times in the string.")
