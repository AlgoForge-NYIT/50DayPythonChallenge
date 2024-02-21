def Pascals_Triangle_v2(rowIndex):
   
    numRows = rowIndex + 1
   
    pascals_triangle = [[1]]
    if numRows == 1:
        return pascals_triangle[0]
    if numRows > 1:
        add_row = pascals_triangle[0][:]
        add_row.append(1)
        pascals_triangle.append(add_row)

       
    i = 2
    while i < numRows:
        row = pascals_triangle[i-1]
        next_row = []
        for j in range(0, len(row) + 1):
            if (j > 0) and (j < len(row)):
                prev_num = row[j-1] # 2 1 0
                curr_num = row[j] # 3 2 1
                next_row.append(prev_num + curr_num)
            else:
                next_row.append(1) # ex. 0, 4
        pascals_triangle.append(next_row)        
        i += 1
       
    if rowIndex < 0 or rowIndex >= len(pascals_triangle):
        return -1
       
    for i in range(len(pascals_triangle)):
        if rowIndex == i:
            return pascals_triangle[i]