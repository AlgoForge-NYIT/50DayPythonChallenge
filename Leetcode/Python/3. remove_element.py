def removeElement(self, nums, val):
    if len(nums) == 0:
        return 0

    write_index = 0

    for i in range(len(nums)): # [1,2,2,2,3], 2 => [1,3]
        if nums[i] != val:
            nums[write_index] = nums[i]
            write_index += 1
    return len(nums[:write_index])