def longest_word_length(words):
    max_length = 0

    for word in words:

        if len(word) > max_length:
            max_length = len(word)
    
    return max_length

user_input = input("Enter numbers separated by spaces: ")

numbers_list = [num for num in user_input.split()]

result = longest_word_length(numbers_list)

# Print the result
print("The length of the longest word is:", result)
