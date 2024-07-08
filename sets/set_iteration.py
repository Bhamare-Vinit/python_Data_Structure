s=set()
n=int(input("Enter the length of set: "))

for i in range(n):
    s.add(input(f"Enter the element at position {i+1} : "))

for i in s:
    print(i)

