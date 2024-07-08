number=int(input("Enter the length of array: "))
arr=[]
for i in range(number):
    arr.append(int(input(f"Enter the element at position {i+1}: ")))

rev=arr
rev.reverse()

arrs=arr
while i<number//2:
    arrs[i],arrs[-i-1]=arrs[-i-1],arrs[i]

sli=[]
sli=arr[::-1]

a=list(reversed(arr))

print(f"Reverse the array using Reverse(): {rev}")
print(f"Reverse the array using Reversed(): {a}")
print(f"Reverse the array using slicing: {sli}")
print(f"Reverse the array using swapping: {arrs}")