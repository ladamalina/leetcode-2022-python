import logging
from typing import List


class Solution:
    @classmethod
    def searchInsert(cls, nums: List[int], target: int) -> int:
        return Solution.searchInsertInterval(nums, target, 0, len(nums) - 1)

    @classmethod
    def searchInsertInterval(cls, nums: List[int], target: int, left_idx: int, right_idx: int) -> int:
        interval_len: int = right_idx - left_idx + 1
        if interval_len == 1:
            if target <= nums[left_idx]:
                return left_idx
            else:
                return left_idx + 1

        mid_left_idx: int = left_idx + interval_len // 2 - 1
        mid_right_idx: int = mid_left_idx + 1
        if target <= nums[mid_left_idx]:
            return Solution.searchInsertInterval(nums, target, left_idx, mid_left_idx)
        elif target < nums[mid_right_idx]:
            return mid_right_idx
        else:
            return Solution.searchInsertInterval(nums, target, mid_right_idx, right_idx)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    assert Solution.searchInsert([1, 3, 5, 6], 5) == 2
    assert Solution.searchInsert([1, 3, 5, 6, 7], 6) == 3
    assert Solution.searchInsert([1, 3, 5, 6, 7], 7) == 4
    assert Solution.searchInsert([1, 3, 5, 6, 7], 1) == 0
    assert Solution.searchInsert([1, 3, 5, 6], 2) == 1
    assert Solution.searchInsert([1, 3, 5, 6], 7) == 4
    assert Solution.searchInsert([1, 3, 5, 6], -1) == 0
    assert Solution.searchInsert([1], 1) == 0
    assert Solution.searchInsert([1], 6) == 1
    assert Solution.searchInsert([1], 1) == 0
