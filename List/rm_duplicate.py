li=[]
number =int(input("Enter the length of list you want to enter: "))
for i in range(number):
    li.append(int(input(f"Enter the element at position {i+1} :")))

s=set()
for i in li:
    s.add(i)

li=list(s)
print(type(li))
print(li)