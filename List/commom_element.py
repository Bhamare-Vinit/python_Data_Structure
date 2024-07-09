def have_common_member(list1, list2):
    # Convert one list to a set for faster lookup
    set1 = set(list1)
    
    # Check for common member
    for item in list2:
        if item in set1:
            return True
    return False

list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
print(have_common_member(list1, list2))  


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print(have_common_member(list1, list2))