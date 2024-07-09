fruits = ("apple", "banana", "cherry","apple")

li=[]
print(f"Following are the repeated elements in tuples: ")
for i in fruits:
    if i not in li:
        li.append(i)
    else:
        print(i)