def contains_dups_II(nums, k):
    # Store the most recent index of each value
    indices = {}
    for i in range(len(nums)):
        num = nums[i]
        if num in indices and i - indices[num] <= k:
            return True
        indices[num] = i
    return False