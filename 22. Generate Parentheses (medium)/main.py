import logging
from typing import List


class Solution:
    INIT_STR: str = ""
    CH_CLOSE: str = ")"
    CH_OPEN: str = "("

    def __init__(self):
        self._all_strings: List[str] = []

    def generateParenthesis(self, n: int) -> List[str]:
        self._all_strings: List[str] = []
        init_opened: int = 0
        self.generate_tree(Solution.INIT_STR, init_opened, init_opened, n, Solution.CH_OPEN)

        return self._all_strings

    def generate_tree(self, init_str: str, init_opened: int, total_opened: int, max_opened: int,
                     next_ch: str) -> None:
        if len(init_str) >= max_opened * 2:
            self._all_strings.append(init_str)
            return
        current_str: str = init_str + next_ch
        current_opened: int = init_opened
        if next_ch == Solution.CH_OPEN:
            current_opened += 1
            total_opened += 1
        else:
            current_opened -= 1

        if total_opened >= max_opened:
            if current_opened == 0:
                self._all_strings.append(current_str)
            else:
                self.generate_tree(current_str, current_opened, total_opened, max_opened, Solution.CH_CLOSE)
        else:
            if current_opened == 0:
                self.generate_tree(current_str, current_opened, total_opened, max_opened, Solution.CH_OPEN)
            else:
                self.generate_tree(current_str, current_opened, total_opened, max_opened, Solution.CH_CLOSE)
                self.generate_tree(current_str, current_opened, total_opened, max_opened, Solution.CH_OPEN)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    expected1 = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    expected1 = sorted(expected1)
    logging.debug(f"expected1 = {expected1}")
    actual1 = Solution().generateParenthesis(3)
    actual1 = sorted(actual1)
    logging.debug(f"actual1 = {actual1}")
    assert len(expected1) == len(actual1)
    for i in range(len(expected1)):
        assert expected1[i] == actual1[i]

    expected2 = ["()"]
    expected2 = sorted(expected2)
    logging.debug(f"expected2 = {expected2}")
    actual2 = Solution().generateParenthesis(1)
    actual2 = sorted(actual2)
    logging.debug(f"actual2 = {actual2}")
    assert len(expected2) == len(actual2)
    for i in range(len(expected2)):
        assert expected2[i] == actual2[i]
