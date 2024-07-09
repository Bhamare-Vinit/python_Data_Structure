def are_circularly_identical(list1, list2):
    # Check if both lists have the same length
    if len(list1) != len(list2):
        return False
    
    concatenated_list1 = list1 + list1
    
    if list2 in concatenated_list1:
        return True
    else:
        return False

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 1, 2]
list3 = [3, 4, 5, 2, 1]

print(are_circularly_identical(list1, list2))  
print(are_circularly_identical(list1, list3))