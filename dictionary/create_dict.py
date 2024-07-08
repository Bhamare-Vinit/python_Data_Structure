number=int(input("Enter the length of dictionary:"))
mydict={}
for i in range(number):
    mydict[i+1]=(i+1)**2

print(mydict)
