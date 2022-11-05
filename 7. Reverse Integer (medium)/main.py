import logging


class Solution:
    @classmethod
    def reverse(cls, x: int) -> int:
        if x == 0:
            return x
        # x != 0

        is_positive: bool = True
        if x < 0:
            is_positive = False
            x = -x

        r = 0
        while x > 0:
            d = x % 10
            x = x // 10
            r = r * 10 + d

        if is_positive:
            r = r if r <= 2 ** 31 - 1 else 0
        else:
            r = -r if r <= 2 ** 31 else 0

        return r


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    assert Solution.reverse(123) == 321
    assert Solution.reverse(-123) == -321
    assert Solution.reverse(120) == 21
    assert Solution.reverse(0) == 0
    assert Solution.reverse(2) == 2
    assert Solution.reverse(-2) == -2
    assert Solution.reverse(1073741824) == 0
    assert Solution.reverse(-1073741824) == 0
    assert Solution.reverse(1534236469) == 0
