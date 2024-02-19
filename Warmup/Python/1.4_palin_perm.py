# check if string is a permutation of a palindrome
# palindrome same forwards and backwards


# check the counts for each letter and check for odd letter counts

def palin_perm(input_string):
    
    # ignore white space and casing
    input_string = ''.join(input_string.split(' ')).lower()
    
    counts = {}
    mulligan = False
    
    # store counts of each char
    for char in input_string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    # iterate through counts
    for key in counts:
        if counts[key] % 2 != 0:
            if mulligan == True:
                return False 
            else:
                mulligan = True
            
    return True

print(palin_perm("Tact Coa")) # ex. taco cat # True
print(palin_perm("Tact Boa")) # false

