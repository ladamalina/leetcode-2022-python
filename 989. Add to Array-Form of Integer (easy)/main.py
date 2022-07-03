import logging
from typing import List


class Solution:
    @classmethod
    def addToArrayForm(cls, num: List[int], k: int) -> List[int]:
        logging.debug(f"num={num}, k={k}")
        over_sum = k
        for i in range(len(num) - 1, -1, -1):
            current_sum = num[i] + over_sum
            if current_sum >= 10:
                over_sum = current_sum // 10
                current_sum = current_sum % 10
            else:
                over_sum = 0
            num[i] = current_sum
        while over_sum > 0:
            num = [over_sum % 10] + num
            over_sum = over_sum // 10
        logging.debug(f"return num={num}")

        return num


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    assert Solution.addToArrayForm([1, 2, 0, 0], 34) == [1, 2, 3, 4]
    assert Solution.addToArrayForm([2, 7, 4], 181) == [4, 5, 5]
    assert Solution.addToArrayForm([2, 1, 5], 806) == [1, 0, 2, 1]
