s=set()
print(type(s))
n=int(input("Enter the length of set: "))

for i in range(n):
    s.add(input(f"Enter the element at position {i+1} : "))
print()
print(f"set is {s}")

