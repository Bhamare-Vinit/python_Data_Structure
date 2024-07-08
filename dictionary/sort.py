my_dict = {2: 'bhree', 
           1: 'two',
           3: 'chree', 
           4: 'ahree', 
           0: 'fhree', }

sorted_dict = sorted(
  my_dict.items(), 
  key = lambda kv: kv[1])
print("Sorted dictionary is based on values:", 
      sorted_dict)

sorted_dict = sorted(
  my_dict.items(), 
  key = lambda kv: kv[1] ,reverse=True)
print("Sorted dictionary in reverse order based on values:", 
      sorted_dict)

sorted_dict = sorted(
  my_dict.items(), 
  key = lambda kv: kv[0])
print("Sorted dictionary is based on key:", 
      sorted_dict)

sorted_dict = sorted(
  my_dict.items(), 
  key = lambda kv: kv[0],reverse=True)
print("Sorted dictionary in reverse order based on key:", 
      sorted_dict)