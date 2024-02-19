def merge(self, nums1, m, nums2, n):
    idx1 = m - 1  # Last non-zero element in nums1
    idx2 = n - 1  # Last element in nums2
    idx_res = m + n - 1  # Last position in nums1

    while idx1 >= 0 and idx2 >= 0:
        if nums1[idx1] > nums2[idx2]:
            nums1[idx_res] = nums1[idx1]
            idx1 -= 1
        else:
            nums1[idx_res] = nums2[idx2]
            idx2 -= 1
        idx_res -= 1

    # Copy remaining elements from nums2, if any
    while idx2 >= 0:
        nums1[idx_res] = nums2[idx2]
        idx2 -= 1
        idx_res -= 1


