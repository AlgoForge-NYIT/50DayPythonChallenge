def twoSum(self, nums, target):
    complements = {}
    for i in range(len(nums)):
        curr = nums[i]
        key = target - nums[i]
        if key in complements:
            return [complements[key], i]
        else:
            complements[curr] = i

