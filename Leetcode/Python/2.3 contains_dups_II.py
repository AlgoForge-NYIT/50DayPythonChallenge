def contains_dups(nums):
    dups_seen = set()
    for num in nums:
        if num in dups_seen:
            return True
        dups_seen.add(num)
    return False