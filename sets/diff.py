set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)

set4 = set1 - set2
print(set4)

set1.difference_update(set2)
print(set1)