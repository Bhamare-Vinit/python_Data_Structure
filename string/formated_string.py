import textwrap

sample_string=input("Enter the string")
# Format the text with a width of 50 characters
formatted_text = textwrap.fill(sample_string, width=50)

# Print the formatted text
print(formatted_text)