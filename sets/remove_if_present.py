thisset = {"apple", "banana", "cherry","a","b"}
target=input("Enter the element you want to remove: ")

if target in thisset:
    thisset.remove(target)
    print{f"Element {target} is removed from the set"}
    print(thisset)

else:
    print("Element not present in set")

