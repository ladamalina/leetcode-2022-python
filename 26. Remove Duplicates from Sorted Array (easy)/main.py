import logging
from typing import List


class Solution:
    @classmethod
    def removeDuplicates(cls, nums: List[int]) -> int:
        logging.debug(f"input: nums = {nums}")
        last_uniq_num = -1000
        uniq_nums_idx = -1

        for i in range(len(nums)):
            if nums[i] > last_uniq_num:
                last_uniq_num = nums[i]
                uniq_nums_idx += 1
                nums[uniq_nums_idx] = nums[i]
        logging.debug(f"updated: nums = {nums}")
        logging.debug(f"uniq_nums_idx = {uniq_nums_idx}")

        return uniq_nums_idx + 1


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    nums1 = [1, 1, 2]
    expected_nums1 = [1, 2]
    k1 = Solution.removeDuplicates(nums1)
    assert k1 == len(expected_nums1)
    for i in range(len(expected_nums1)):
        assert nums1[i] == expected_nums1[i]

    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected_nums2 = [0, 1, 2, 3, 4]
    k2 = Solution.removeDuplicates(nums2)
    assert k2 == len(expected_nums2)
    for i in range(len(expected_nums2)):
        assert nums2[i] == expected_nums2[i]
