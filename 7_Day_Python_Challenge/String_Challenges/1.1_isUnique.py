def isUnique(input_str):
    for i in range(len(input_str)):
        for j in range(i+1, len(input_str)):
            if input_str[i] == input_str[j]:
                return False
    return True

print(isUnique('abcd')) # True
print(isUnique('aabd')) # False
print(isUnique('abdd')) # False