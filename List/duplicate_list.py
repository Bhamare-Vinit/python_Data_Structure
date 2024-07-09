def remove_duplicates(list_of_lists):
    unique_lists = []

    seen = set()
    
    for lst in list_of_lists:

        tuple_lst = tuple(lst)
        if tuple_lst not in seen:
            seen.add(tuple_lst)
            unique_lists.append(lst)
    
    return unique_lists

# Sample list
sample_list = [[10, 20], [40], [30, 56, 25], [10,20], [33], [40]]

# Remove duplicates
new_list = remove_duplicates(sample_list)

# Print the new list
print("New List:", new_list)
