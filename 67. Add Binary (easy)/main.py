import logging
from typing import List


class Solution:
    @classmethod
    def addBinary(cls, a: str, b: str) -> str:
        logging.debug(f"a={a}, b={b}")
        if a == "0":
            return b
        if b == "0":
            return a

        if len(a) > len(b):
            res: str = a
            add: str = b
        else:
            res: str = b
            add: str = a
        # len(add) <= len(res)

        over_sum_int: int = 0
        over_sum_bin: str = "0"

        sum_list: List[str] = []

        i: int = 0
        while i < len(res) or i < len(add):
            res_i = len(res) - i - 1
            add_i = len(add) - i - 1

            res_str: str = res[res_i]
            res_int: int = int(res_str, 2)

            add_int: int = 0
            if i < len(add):
                add_str: str = add[add_i]
                add_int = int(add_str, 2)

            current_sum_int: int = res_int + add_int + over_sum_int
            current_sum_bin: str = bin(current_sum_int)[2:]
            if len(current_sum_bin) > 1:
                over_sum_bin = current_sum_bin[:-1]
                over_sum_int = int(over_sum_bin, 2)
                current_sum_bin = current_sum_bin[-1]
            else:
                over_sum_bin = "0"
                over_sum_int = 0
            # res[res_i] = current_sum_bin
            sum_list.append(current_sum_bin)
            i += 1

        if len(over_sum_bin) > 0 and over_sum_bin != "0":
            sum_list.append(over_sum_bin)

        sum_str: str = "".join(sum_list[::-1])

        return sum_str


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    assert Solution.addBinary("11", "1") == "100"
    assert Solution.addBinary("1010", "1011") == "10101"
    assert Solution.addBinary("0", "0") == "0"
    assert Solution.addBinary("100", "110010") == "110110"
