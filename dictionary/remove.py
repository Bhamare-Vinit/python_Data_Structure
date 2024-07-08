
number=int(input("Enter the length of dictionary:"))
mydict={}
for i in range(number):
    key=input(f"Enter the key for pair {i+1}: ")
    value=input(f"Enter the value for pair {i+1}: ")
    mydict[key]=value
print(mydict)
print("-"*50)
delete=input("Enter the key you want to delete: ")

if delete in mydict:
    del mydict[delete]
else:
    print(f"{delete} is not present in dictionary")
print(mydict)