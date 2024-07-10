def replace_char(s):
    first_char = s[0]
    modified_string = first_char + s[1:].replace(first_char, '$')
    return modified_string

sample_string = input("Enter the string: ")
result = replace_char(sample_string)
print(result)
