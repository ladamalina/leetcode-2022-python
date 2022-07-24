import logging
from typing import List


class Solution:
    @classmethod
    def plusOne(cls, digits: List[int]) -> List[int]:
        logging.debug(f"digits={digits}")
        over_sum = 1
        for i in range(len(digits) - 1, -1, -1):
            current_sum = digits[i] + over_sum
            if current_sum >= 10:
                over_sum = current_sum // 10
                current_sum = current_sum % 10
            else:
                over_sum = 0
            digits[i] = current_sum
        if over_sum > 0:
            digits = [over_sum] + digits
        logging.debug(f"return digits={digits}")

        return digits


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    assert Solution.plusOne([1, 2, 3]) == [1, 2, 4]
    assert Solution.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert Solution.plusOne([9, 9, 9]) == [1, 0, 0, 0]
