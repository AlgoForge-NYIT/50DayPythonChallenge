def check_permute(str_one, str_two):
    char_counts1 = {}
    for char in str_one:
        if char in char_counts1:
            char_counts1[char] += 1
        else:
            char_counts1[char] = 1  

    char_counts2 = {}
    for char in str_two:
        if char in char_counts2:
            char_counts2[char] += 1
        else:
            char_counts2[char] = 1
    
    return char_counts1 == char_counts2

print(check_permute('hello world', 'world hello')) # True
print(check_permute('mountain top', 'stop mountain')) # False

print(check_permute('aab', 'aba')) # True
print(check_permute('aaab', 'aabb')) # False