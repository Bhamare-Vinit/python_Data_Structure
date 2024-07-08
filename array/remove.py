number=int(input("Enter the length of array: "))
arr=[]
for i in range(number):
    arr.append(int(input(f"Enter the element at position {i+1}: ")))
target=int(input("Enter the element to delete from the list: "))

for i in arr:
    if i == target:
        arr.remove(target)
        break

print(arr)