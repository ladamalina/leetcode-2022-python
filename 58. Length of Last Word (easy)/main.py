import logging


class Solution:
    @classmethod
    def lengthOfLastWord(cls, s: str) -> int:
        last_ch_i: int = len(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if last_ch_i == len(s):
                    continue
                else:
                    return last_ch_i - i
            else:
                if last_ch_i == len(s):
                    last_ch_i = i
                if i == 0:
                    return last_ch_i + 1

        return len(s)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    assert Solution.lengthOfLastWord("Hello World") == 5
    assert Solution.lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert Solution.lengthOfLastWord("luffy is still joyboy") == 6
    assert Solution.lengthOfLastWord("a") == 1
    assert Solution.lengthOfLastWord("aaa") == 3
    assert Solution.lengthOfLastWord("aaa  ") == 3
    assert Solution.lengthOfLastWord("   aaa") == 3
    assert Solution.lengthOfLastWord("   a") == 1
    assert Solution.lengthOfLastWord("a   ") == 1
