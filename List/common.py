def find_common_items(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_items = list(set1.intersection(set2))
    return common_items

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_items = find_common_items(list1, list2)
print("Common items:", common_items)