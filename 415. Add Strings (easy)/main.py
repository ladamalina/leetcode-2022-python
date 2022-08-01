import logging
from typing import List


class Solution:
    @classmethod
    def addStrings(cls, num1: str, num2: str) -> str:
        logging.debug(f"num1 = {num1}, num2 = {num2}")
        if num1 == "0":
            return num2
        if num2 == "0":
            return num1

        if len(num1) > len(num2):
            res: str = num1
            add: str = num2
        else:
            res: str = num2
            add: str = num1
        # len(add) <= len(res)
        logging.debug(f"res = {res}, add = {add}")

        over_sum_int: int = 0
        sum_list: List[str] = []

        i: int = 0
        while i < len(res) or i < len(add):
            res_i = len(res) - i - 1
            add_i = len(add) - i - 1

            res_int: int = int(res[res_i])
            add_int: int = 0
            if i < len(add):
                add_int = int(add[add_i])

            current_sum_int: int = res_int + add_int + over_sum_int
            if current_sum_int >= 10:
                over_sum_int = current_sum_int // 10
                current_sum_int = current_sum_int % 10
            else:
                over_sum_int = 0

            sum_list.append(current_sum_int)
            i += 1

        if over_sum_int > 0:
            sum_list.append(over_sum_int)
        logging.debug(f"sum_list = {sum_list}")

        sum_str: str = "".join([str(_) for _ in sum_list[::-1]])
        logging.debug(f"sum_str = {sum_str}")

        return sum_str


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    assert Solution.addStrings("11", "123") == "134"
    assert Solution.addStrings("456", "77") == "533"
    assert Solution.addStrings("0", "0") == "0"
    assert Solution.addStrings("999", "1") == "1000"
