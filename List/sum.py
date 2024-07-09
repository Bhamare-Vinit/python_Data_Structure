# user_input = input("Enter numbers separated by spaces: ")

# # Splitting the input string into individual elements and converting them to integers
# numbers_list = [int(num) for num in user_input.split()]
li=[]
number =int(input("Enter the length of list you want to enter: "))
for i in range(number):
    li.append(int(input(f"Enter the element at position {i+1} :")))

total_sum=sum(li)
print(f"The sum of all the elements of list is {total_sum}")