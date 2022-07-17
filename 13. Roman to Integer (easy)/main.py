import logging
from typing import Dict


class Solution:
    ch_to_int: Dict[str, int] = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    @classmethod
    def romanToInt(cls, s: str) -> int:
        res: int = 0
        i: int = len(s) - 1
        while i >= 0:
            ch_val: int = Solution.ch_to_int[s[i]]
            if i == 0:
                res += ch_val
                break
            if s[i] in {"V", "X"} and s[i - 1] == "I":
                ch_val -= 1
                i -= 1
            if s[i] in {"L", "C"} and s[i - 1] == "X":
                ch_val -= 10
                i -= 1
            if s[i] in {"D", "M"} and s[i - 1] == "C":
                ch_val -= 100
                i -= 1

            res += ch_val
            i -= 1

        return res


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    assert Solution.romanToInt("III") == 3
    assert Solution.romanToInt("LVIII") == 58
    assert Solution.romanToInt("MCMXCIV") == 1994
