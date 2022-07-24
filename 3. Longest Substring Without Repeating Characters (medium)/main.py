import logging
from typing import Dict


class Solution:
    @classmethod
    def lengthOfLongestSubstring(cls, s: str) -> int:
        if len(s) == 0:
            return 0

        longest_seq = 0
        current_seq = 0
        chars_to_idx: Dict[str, int] = {}
        begin_idx = 0
        i = 0
        while i < len(s):
            if s[i] in chars_to_idx:  # double char
                if current_seq > longest_seq:
                    longest_seq = current_seq
                double_char_first_idx = chars_to_idx[s[i]]
                for j in range(begin_idx, double_char_first_idx + 1):
                    del chars_to_idx[s[j]]
                begin_idx = double_char_first_idx + 1
                chars_to_idx[s[i]] = i
                current_seq = i - double_char_first_idx
            else:  # unique char
                chars_to_idx[s[i]] = i
                current_seq += 1
            i += 1
        if current_seq > longest_seq:
            longest_seq = current_seq

        return longest_seq


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    assert Solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution.lengthOfLongestSubstring("bbbbb") == 1
    assert Solution.lengthOfLongestSubstring("pwwkew") == 3
    assert Solution.lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyz") == 26
