def single_num(nums):
    counts = {}
    # store counts
    for i in range(len(nums)):
        if nums[i] in counts:
            counts[nums[i]] += 1
        else:
            counts[nums[i]] = 1

    # return element without count of 2
    for ele in counts:
        if counts[ele] != 2:
            return ele