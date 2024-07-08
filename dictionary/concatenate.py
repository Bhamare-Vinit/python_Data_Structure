dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

#using update
dic2.update(dic1)
dic3.update(dic2)
print(f"dictionary using 'update' :{dic3}")

#using unpacking operator
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={**dic1,**dic2,**dic3}

print(f"dictionary using unpacking uperator :{dic4}")

#using |
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4=dic1|dic2|dic3

print(f"dictionary using | :{dic4}")
