def removeDuplicates(self, nums):
        # loop and have a global index of when the next unique num should start
        uniq_num_index = 0
        for i in range(len(nums)):
            if nums[uniq_num_index] != nums[i]:
                uniq_num_index += 1
                nums[uniq_num_index] = nums[i] # [1, 2, 2, 3, 3] => [1, 2, 3, 3, 3]
        return uniq_num_index + 1

