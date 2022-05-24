import logging
from typing import List


class Solution:
    @classmethod
    def removeElement(cls, nums: List[int], val: int) -> int:
        result_nums_idx = -1

        for i in range(len(nums)):
            if nums[i] != val:
                result_nums_idx += 1
                nums[result_nums_idx] = nums[i]

        return result_nums_idx + 1


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    nums1 = [3, 2, 2, 3]
    val1 = 3
    expected_nums1 = [2, 2]
    k1 = Solution.removeElement(nums1, val1)
    assert k1 == len(expected_nums1)
    nums1[:k1] = sorted(nums1[:k1])
    logging.debug(f"expected_nums1 = {expected_nums1}")
    logging.debug(f"nums1 = {nums1}")
    for i in range(len(expected_nums1)):
        assert nums1[i] == expected_nums1[i]
    logging.debug("." * 40)

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    expected_nums2 = [0, 0, 1, 3, 4]
    k2 = Solution.removeElement(nums2, val2)
    assert k2 == len(expected_nums2)
    nums2[:k2] = sorted(nums2[:k2])
    logging.debug(f"expected_nums2 = {expected_nums2}")
    logging.debug(f"nums2 = {nums2}")
    for i in range(len(expected_nums2)):
        assert nums2[i] == expected_nums2[i]
    logging.debug("." * 40)

    nums3 = [0, 0, 0, 0, 0, 0, 0, 0]
    val3 = 0
    expected_nums3 = []
    k3 = Solution.removeElement(nums3, val3)
    assert k3 == len(expected_nums3)
    nums3[:k3] = sorted(nums3[:k3])
    logging.debug(f"expected_nums3 = {expected_nums3}")
    logging.debug(f"nums3 = {nums3}")
    for i in range(len(expected_nums3)):
        assert nums3[i] == expected_nums3[i]
