import logging
import math


class Solution:
    @classmethod
    def isPalindrome(cls, x: int) -> bool:
        logging.debug(f"isPalindrome(x={x}) " + "." * 40)
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False

        digits_num = int(math.log10(x)) + 1
        half_digits_num = digits_num // 2
        logging.debug(f"half_digits_num = {half_digits_num}")

        # x = 123 454 321
        if digits_num % 2:
            left_half = x // 10**(half_digits_num+1)
        else:
            left_half = x // 10**half_digits_num
        right_half = x % 10**half_digits_num
        logging.debug(f"left_half = {left_half}, right_half = {right_half}")

        reverted_right = 0
        for i in range(half_digits_num):
            reverted_right += (right_half % 10) * 10**(half_digits_num-i-1)
            right_half = right_half // 10
        logging.debug(f"reverted_right = {reverted_right}")

        return left_half == reverted_right


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    assert Solution.isPalindrome(123454321)
    assert Solution.isPalindrome(123455321) is False
    assert Solution.isPalindrome(1234554321)
    assert Solution.isPalindrome(1234564321) is False
    assert Solution.isPalindrome(121)
    assert Solution.isPalindrome(1)
    assert Solution.isPalindrome(77)
    assert Solution.isPalindrome(10) is False
    assert Solution.isPalindrome(-121) is False
    assert Solution.isPalindrome(123) is False
    assert Solution.isPalindrome(120021)
    assert Solution.isPalindrome(1230321)
