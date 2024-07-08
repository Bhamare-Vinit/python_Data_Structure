string=input("Enter the string :")

dic={}
for char in string:
    if char in dic:
        dic[char]+=1
    else:
        dic[char]=1

print(dic)
