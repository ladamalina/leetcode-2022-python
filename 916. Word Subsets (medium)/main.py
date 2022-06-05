import logging
from typing import List


class Solution:
    CODE_LEN: int = 26

    @classmethod
    def wordSubsets(cls, words1: List[str], words2: List[str]) -> List[str]:
        universal_code: List[int] = [0] * Solution.CODE_LEN
        for w in words2:
            w_code: List[int] = Solution.get_code(w)
            for i in range(Solution.CODE_LEN):
                universal_code[i] = max(universal_code[i], w_code[i])

        result: List[str] = []
        for w1 in words1:
            w1_code = Solution.get_code(w1)
            w1_is_universal: bool = True
            for i in range(Solution.CODE_LEN):
                if w1_code[i] < universal_code[i]:
                    w1_is_universal = False
                    break
            if w1_is_universal:
                result.append(w1)

        return result

    @classmethod
    def get_code(cls, word: str) -> List[int]:
        code = [0] * Solution.CODE_LEN
        for ch in word:
            code[ord(ch) - ord("a")] += 1

        return code


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    expected_res1 = ["facebook", "google", "leetcode"]
    actual_res1 = Solution.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"],
                                       ["e", "o"])
    logging.debug(f"expected_res1 = {expected_res1}")
    logging.debug(f"actual_res1 = {actual_res1}")
    assert expected_res1 == actual_res1
    logging.debug("." * 40)

    expected_res2 = ["apple", "google", "leetcode"]
    actual_res2 = Solution.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"],
                                       ["l", "e"])
    logging.debug(f"expected_res2 = {expected_res2}")
    logging.debug(f"actual_res2 = {actual_res2}")
    assert expected_res2 == actual_res2
    logging.debug("." * 40)

    expected_res3 = ["cccbb", "aacbc", "bbccc", "acaba"]
    actual_res3 = Solution.wordSubsets(["cccbb", "aacbc", "bbccc", "baaba", "acaba"],
                                       ["cb", "b", "cb"])
    logging.debug(f"expected_res3 = {expected_res3}")
    logging.debug(f"actual_res3 = {actual_res3}")
    assert expected_res3 == actual_res3
    logging.debug("." * 40)
