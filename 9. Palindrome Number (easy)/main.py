import logging
import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
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

    s = Solution()
    assert s.isPalindrome(123454321)
    assert s.isPalindrome(123455321) is False
    assert s.isPalindrome(1234554321)
    assert s.isPalindrome(1234564321) is False
    assert s.isPalindrome(121)
    assert s.isPalindrome(1)
    assert s.isPalindrome(77)
    assert s.isPalindrome(10) is False
    assert s.isPalindrome(-121) is False
    assert s.isPalindrome(123) is False
    assert s.isPalindrome(120021)
    assert s.isPalindrome(1230321)
