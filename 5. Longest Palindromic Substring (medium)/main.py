import logging
from typing import Dict, Tuple


class Solution:
    def __init__(self):
        self._longest_left_idx: int = 0
        self._longest_right_idx: int = 0
        self._longest_len: int = 0
        self._longest_half_len: int = 0

    def _get_longest_palindrome(self, s: str, mid_i_left: int, mid_i_right: int) -> Tuple[int, int]:
        while True:
            mid_i_left -= 1
            mid_i_right += 1
            if mid_i_left < 0 or mid_i_right >= len(s) or s[mid_i_left] != s[mid_i_right]:
                break
        mid_i_left += 1
        mid_i_right -= 1

        return mid_i_left, mid_i_right

    def _update_longest_palindrome(self, left_idx: int, right_idx: int) -> None:
        current_len: int = right_idx - left_idx + 1
        if current_len > self._longest_len:
            self._longest_left_idx = left_idx
            self._longest_right_idx = right_idx
            self._longest_len = current_len
            self._longest_half_len = self._longest_len // 2

    def longestPalindrome(self, s: str) -> str:
        logging.debug(f"s = {s}")
        for i in range(len(s)):
            if len(s) - 1 < self._longest_half_len:
                break
            if i + 1 < len(s) and s[i] == s[i + 1]:
                left_idx, right_idx = self._get_longest_palindrome(s, i, i + 1)
                self._update_longest_palindrome(left_idx, right_idx)
            if i - 1 >= 0 and i + 1 < len(s) and s[i - 1] == s[i + 1]:
                left_idx, right_idx = self._get_longest_palindrome(s, i - 1, i + 1)
                self._update_longest_palindrome(left_idx, right_idx)
        longest_str: str = s[self._longest_left_idx:self._longest_right_idx + 1]
        logging.debug(f"longest_str = {longest_str}")

        return longest_str


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    assert Solution().longestPalindrome("babad") == "bab"
    assert Solution().longestPalindrome("cbbd") == "bb"
    assert Solution().longestPalindrome("a") == "a"
    assert Solution().longestPalindrome("aaaa") == "aaaa"
    assert Solution().longestPalindrome("aaaaa") == "aaaaa"
