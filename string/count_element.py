def character_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    return freq

sample_string=input("Enter  thr string: ")
# sample_string = "google.com"
result = character_frequency(sample_string)


print(result)
