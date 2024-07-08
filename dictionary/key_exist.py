
sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
conti=True

keys_to_check = input("Enter keys to check (comma-separated): ").strip().split(',')

for i in keys_to_check:
    if i not in sample_dict:
        conti=False

if conti:
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")
