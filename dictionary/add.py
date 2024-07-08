mydi={0: 10, 1: 20}
# mydi[2]=30
# print(mydi)
number=int(input("Inter the number of key and value pair user wants to add:"))
for i in range(number):
    key=int(input(f"Enter the Key for pair {i+1}:"))
    value=int(input(f"Enter the value for pair {i+1}:"))
    mydi[key]=value
print(f"Updated dictionary :",mydi)