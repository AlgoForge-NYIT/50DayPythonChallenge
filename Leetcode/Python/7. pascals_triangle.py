def Pascals_Triangle(numRows):
   
    result = [[1]]
    if numRows == 1:
        return result
    if numRows > 1:
        add_row = result[0][:]
        add_row.append(1)
        result.append(add_row)
        if numRows == 2:
            return result
       
    i = 2
    while i < numRows:
        row = result[i-1]
        next_row = []
        for j in range(0, len(row) + 1):
            if (j > 0) and (j < len(row)):
                prev_num = row[j-1] # 2 1 0
                curr_num = row[j] # 3 2 1
                next_row.append(prev_num + curr_num)
            else:
                next_row.append(1) # ex. 0, 4
        result.append(next_row)        
        i += 1
    return result