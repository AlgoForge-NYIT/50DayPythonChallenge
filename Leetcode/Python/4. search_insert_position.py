def search_insert_recursive(left, right):
    if left > right:
        return left


    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    if target < nums[mid]:
        return search_insert_recursive(left, mid - 1)
    else:
        return search_insert_recursive(mid + 1, right)

    return search_insert_recursive(0, len(nums) - 1)


    ### ITERATIVE METHOD ###


    def search_insert(nums, target):
    left = 0
    right = len(nums) - 1
 
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target: # num found
            return mid

        elif target < nums[mid]: # go left half or right half
            right = mid - 1
        else:
            left = mid + 1
    return left