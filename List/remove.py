Sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# del Sample_List[4]
# del Sample_List[3]
# Sample_List.pop(0)
# print(Sample_List)

user_input = input("Enter index numbers you want to delete separated by spaces: ")

# Splitting the input string into individual elements and converting them to integers
numbers_list = [int(num) for num in user_input.split()]
print(numbers_list)

# for i in range(0,len(numbers_list)):
#     print(numbers_list[i])
for i in range(len(numbers_list)-1,-1,-1):
    Sample_List.pop(numbers_list[i])
    print(numbers_list[i])



print(Sample_List)