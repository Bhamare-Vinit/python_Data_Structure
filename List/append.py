list1 = [1, 2, 3]
list2 = [3, 4, 5]

for x in list1:
    list2.append(x)
print(f"Merged two list using append :{list2}")

list3=list1+list2
print(f"Merged two list using '+' operator:{list3}")

list2.extend(list1)
print(f"Merged two list using extend :{list2}")