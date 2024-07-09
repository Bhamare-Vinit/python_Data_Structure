sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Sorting the list by the last element in each tuple
sorted_list = sorted(sample_list, key=lambda x: x[-1])

# Printing the sorted list
print("Sorted list:", sorted_list)