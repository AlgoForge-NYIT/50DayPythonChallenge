
# check if one string is a rotation of another:
# ex. terbottle|wat is a rotation of waterbottle 

def isSubstring(string_one, string_two):
    # concatenate the string
    # ex wa|terbottlewat|erbottle. 
    
    if len(string_one) != len(string_two):
        return False

    double_string = string_one + string_two

    for i in range(len(string_one) + 1):
        slice_string = double_string[i:i + len(string_one)]
        if slice_string == string_two: # second string found in the double string
            return True
    return False

print(isSubstring('waterbottle', 'terbottlewa')) # True
print(isSubstring('waterbottle', 'sterbottlewat')) # False
print(isSubstring('helloworld', 'worldhello')) # True
print(isSubstring('helloworld', 'worldhome')) # False