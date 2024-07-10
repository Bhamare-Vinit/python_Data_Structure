def get_last_part_before_char(s, char):
    # Find the last occurrence of the specified character
    index = s.rfind(char)
    
    # If the character is found, return the substring before it
    if index != -1:
        return s[:index]
    # If the character is not found, return the original string
    else:
        return s
    
s=input("Enter the String :")
char=input("Enter the character :")

print(f"String before specified character is : {get_last_part_before_char(s,char)}")
