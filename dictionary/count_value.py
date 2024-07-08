sample_data = [
    {'id': 1, 'success': True, 'name': 'Lary'},
    {'id': 2, 'success': False, 'name': 'Rabi'},
    {'id': 3, 'success': False, 'name': 'Alex'}
]

# Count the number of dictionaries with 'success' as True
success_count = 0
for item in sample_data:
    if item.get("success")==True:
        success_count+=1

# Print the result
print(f"Count of dictionaries with success as True: {success_count}")