Sample_List = ['abc', 'xyz', 'aba', '1221']
count=0
for i in Sample_List:
    if (len(i)>=2) and (i[0]==i[-1]):
        count+=1
print(f"There are {count} pairs having string length is 2 or more and the first and last character are same")