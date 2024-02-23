def majority_element(nums):
    counts = {} # create a counts obj
   
    for i in range(len(nums)):
        if nums[i] in counts:
            counts[nums[i]] += 1
        else:
            counts[nums[i]] = 1
    # loop through counts
    for ele in counts:
        count = counts[ele]
        if count > len(nums) / 2:
            return ele
   
    return -1