import logging
from typing import List


class Solution:
    @classmethod
    def merge(cls, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        idx1 = m - 1
        idx2 = n - 1
        target_idx = len(nums1) - 1
        while idx1 >= 0 and idx2 >= 0:
            if nums1[idx1] >= nums2[idx2]:
                nums1[target_idx] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[target_idx] = nums2[idx2]
                idx2 -= 1
            target_idx -= 1

        if idx2 >= 0:
            while idx2 >= 0:
                nums1[target_idx] = nums2[idx2]
                idx2 -= 1
                target_idx -= 1


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    expected_nums1 = [1,2,2,3,5,6]
    Solution.merge(nums1, m, nums2, n)
    assert expected_nums1 == nums1

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    expected_nums1 = [1]
    Solution.merge(nums1, m, nums2, n)
    assert expected_nums1 == nums1

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    expected_nums1 = [1]
    Solution.merge(nums1, m, nums2, n)
    assert expected_nums1 == nums1
