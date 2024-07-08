s=set()
n=int(input("Enter the length of set: "))
v=["Om","Bhamare"]

for i in range(n):
    s.add(input(f"Enter the element at position {i+1} : "))

s.add("vinit")

s.update(v)

print(s)

