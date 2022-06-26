import logging
from typing import Dict, List


class Solution:
    @classmethod
    def twoSum(cls, nums: List[int], target: int) -> List[int]:
        umap: Dict[int, int] = {}
        for i in range(len(nums)):
            pair_to_find = target - nums[i]
            if pair_to_find in umap:
                return [umap[pair_to_find], i]
            else:
                umap[nums[i]] = i
        return []


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    nums1 = [2, 7, 11, 15]
    target1 = 9
    expected_indices1 = [0, 1]
    assert expected_indices1 == Solution.twoSum(nums1, target1)

    nums2 = [3, 2, 4]
    target2 = 6
    expected_indices2 = [1, 2]
    assert expected_indices2 == Solution.twoSum(nums2, target2)

    nums3 = [3, 3]
    target3 = 6
    expected_indices3 = [0, 1]
    assert expected_indices3 == Solution.twoSum(nums3, target3)
