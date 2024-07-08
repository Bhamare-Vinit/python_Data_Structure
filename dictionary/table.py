number=int(input("Enter the length of dictionary:"))
mydict={}
for i in range(number):
    key=input(f"Enter the key for pair {i+1}: ")
    value=input(f"Enter the value for pair {i+1}: ")
    mydict[key]=value

print("-"*37)
print(f"| {'Key':^15} | {'Values':^15} |")
print("-"*37)
for i in mydict:
    print(f"| {i:^15} | {mydict[i]:^15} |")
    print("-"*37)
