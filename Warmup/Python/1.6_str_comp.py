# compress a string with repeated characters
# only upper and lower case letters used 
# ex . aabbbccccc becomes a2b3c5


# loop and get the counts
# once the character changes, append the letter and its count to a runnning string
# return the compressed string if shorter than original string


def str_comp(input_string):
    compressed_string = ''
    max_count = 1
    prev_count = 1
    prev_char = input_string[0]


    for char in input_string[1:]:
        if prev_char != char:
            compressed_string += (prev_char + str(prev_count)) #ex. a5
            
            max_count = max(max_count, prev_count)# update max count
            prev_char = char # reset values
            prev_count = 1

            
        else:
            prev_count += 1
    # update max count based on last character in string
    max_count = max(max_count, prev_count)
    compressed_string += (prev_char + str(prev_count))
    
    return compressed_string if max_count != 1 else input_string

print(str_comp('aabbbccccc')) # a2b3c5
print(str_comp('abcd')) # abcd