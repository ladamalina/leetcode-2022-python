import logging
from typing import List


class Solution:
    @classmethod
    def is_char_eq(cls, strs: List[str], char_idx: int) -> bool:
        logging.debug(f"is_char_eq: strs = {strs}, char_idx = {char_idx}")
        for str_idx in range(len(strs)):
            if str_idx == 0:
                continue
            if char_idx >= len(strs[str_idx]) or char_idx >= len(strs[str_idx - 1]):
                return False
            if strs[str_idx][char_idx] != strs[str_idx - 1][char_idx]:
                return False
        return True

    @classmethod
    def longestCommonPrefix(cls, strs: List[str]) -> str:
        logging.debug(f"longestCommonPrefix: strs = {strs}")
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        char_idx = 0
        while True:
            if not cls.is_char_eq(strs, char_idx):
                break
            char_idx += 1

        longest_common = strs[0][:char_idx]
        logging.debug(f"longestCommonPrefix: longest_common = {longest_common}")
        return longest_common


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    assert Solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert Solution.longestCommonPrefix(["flower", "flower", "flower"]) == "flower"
    assert Solution.longestCommonPrefix(["flower", "flow", ""]) == ""
    assert Solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert Solution.longestCommonPrefix(["racecar"]) == "racecar"
    assert Solution.longestCommonPrefix(["", "", ""]) == ""
    assert Solution.longestCommonPrefix([]) == ""
    assert Solution.longestCommonPrefix(["","b"]) == ""
