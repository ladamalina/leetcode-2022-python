import logging
from typing import List


class Solution:
    @classmethod
    def moveZeroes(cls, nums: List[int]):
        logging.debug(f"input: nums = {nums}")
        result_nums_idx = -1

        for i in range(len(nums)):
            if nums[i] != 0:
                result_nums_idx += 1
                nums[result_nums_idx] = nums[i]

        while result_nums_idx > -1 and result_nums_idx + 1 < len(nums):
            result_nums_idx += 1
            if nums[result_nums_idx] != 0:
                nums[result_nums_idx] = 0


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    nums1 = [0, 1, 0, 3, 12]
    expected_nums1 = [1, 3, 12, 0, 0]
    Solution.moveZeroes(nums1)
    for i in range(len(expected_nums1)):
        assert nums1[i] == expected_nums1[i]

    nums2 = [0]
    expected_nums2 = [0]
    Solution.moveZeroes(nums2)
    for i in range(len(expected_nums2)):
        assert nums2[i] == expected_nums2[i]

    nums3 = [0, 0, 0]
    expected_nums3 = [0, 0, 0]
    Solution.moveZeroes(nums3)
    for i in range(len(expected_nums3)):
        assert nums3[i] == expected_nums3[i]
