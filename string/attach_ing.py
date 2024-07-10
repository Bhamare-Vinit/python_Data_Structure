def add_suffix(s):
    if len(s) < 3:
        return s
    elif s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'

sample_string1 =input("Enter the string :")

result1 = add_suffix(sample_string1)

print(result1) 
