number=int(input("Enter the length of array: "))
arr=[]
for i in range(number):
    arr.append(int(input(f"Enter the element at position {i+1}: ")))

print(arr)
for i in range(len(arr)):
    print(f"The element at position {i+1} is {arr[i]}")
    print("-"* 50)