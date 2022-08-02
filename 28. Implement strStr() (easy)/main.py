import logging


class Solution:
    @classmethod
    def strStr(cls, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        i: int = 0
        while i < len(haystack):
            if i + len(needle) > len(haystack):
                return -1
            if haystack[i] != needle[0]:
                i += 1
                continue

            # haystack[i] == needle[0]
            if len(needle) == 1:
                return i
            for ni in range(1, len(needle)):
                hi: int = i + ni
                if haystack[hi] == needle[ni]:
                    if ni == len(needle) - 1:
                        return i
                else:
                    break
            i += 1

        return -1


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    assert Solution.strStr("hello", "ll") == 2
    assert Solution.strStr("aaaaa", "bba") == -1
    assert Solution.strStr("abcabc", "abcd") == -1
    assert Solution.strStr("abcabcdabcd", "abcd") == 3
    assert Solution.strStr("a", "a") == 0
    assert Solution.strStr("aa", "aaa") == -1
    assert Solution.strStr("mississippi", "sippia") == -1
