import logging
from typing import List


class Solution:
    @classmethod
    def sortedSquares(self, nums: List[int]) -> List[int]:
        logging.debug(f"nums = {nums}")
        if not nums:
            return nums
        if len(nums) == 1:
            return [nums[0]**2]
        mid_idx = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                mid_idx = i + 1
            nums[i] = nums[i]**2
        logging.debug(f"mid_idx = {mid_idx}")

        result: List[int] = [0] * len(nums)
        result_idx = 0
        left_mid_idx = mid_idx - 1
        while left_mid_idx >= 0 and mid_idx < len(nums):
            if nums[left_mid_idx] >= nums[mid_idx]:
                result[result_idx] = nums[mid_idx]
                mid_idx += 1
            else:
                result[result_idx] = nums[left_mid_idx]
                left_mid_idx -= 1
            result_idx += 1
        while left_mid_idx >= 0:
            result[result_idx] = nums[left_mid_idx]
            left_mid_idx -= 1
            result_idx += 1
        while mid_idx < len(nums):
            result[result_idx] = nums[mid_idx]
            mid_idx += 1
            result_idx += 1
        logging.debug(f"result = {result}")

        return result


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    assert Solution.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert Solution.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]
    assert Solution.sortedSquares([-7,-3]) == [9,49]
    assert Solution.sortedSquares([3,4]) == [9,16]
    assert Solution.sortedSquares([]) == []
    assert Solution.sortedSquares([-3]) == [9]
    assert Solution.sortedSquares([3]) == [9]
