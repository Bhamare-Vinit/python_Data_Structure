thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

rev_tuple=thistuple[::-1]
print(f"Original tuple is : {thistuple}")
print(f"Reversed tuple is using slicing :{rev_tuple}")

#another method
li=[]
for i in range(len(thistuple)-1,-1,-1):
    li.append(thistuple[i])
rev2_tuple=tuple(li)
print(f"Reversed tuple using loop :{rev2_tuple}")