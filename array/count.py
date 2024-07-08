number=int(input("Enter the length of array: "))
target= int(input("Enter the number to find in array: "))
arr=[]
count=0
for i in range(number):
    arr.append(int(input(f"Enter the element at position {i+1}: ")))

for i in arr:
    if i==target:
        count+=1

print(f"The element {target} occurs {count} times in the array.")
