import logging
from typing import List


class Solution:
    @classmethod
    def threeConsecutiveOdds(cls, arr: List[int]) -> bool:
        odds_len: int = 0
        for num in arr:
            if num % 2 == 1:
                odds_len += 1
                if odds_len >= 3:
                    return True
            else:
                odds_len = 0

        return False


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    assert Solution.threeConsecutiveOdds([2, 6, 4, 1]) is False
    assert Solution.threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]) is True
