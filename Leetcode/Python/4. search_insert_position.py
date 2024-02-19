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