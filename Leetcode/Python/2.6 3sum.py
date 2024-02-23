def threeSum(nums):
    result_lists = []
    nums.sort()
    indices = {num: idx for idx, num in enumerate(nums)}

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for the first number
            continue

        for j in range(i + 1, len(nums)):
            if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicates for the second number
                continue

            num1 = nums[i]
            num2 = nums[j]
            target = -(num1 + num2)

            # Use the indices dictionary to check if the target is at a location after the j index
            if target in indices and indices[target] > j:
                triplet = [num1, num2, target]
                result_lists.append(triplet)
               

    return result_lists