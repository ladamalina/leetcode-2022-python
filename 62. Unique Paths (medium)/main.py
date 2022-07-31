import logging
import math


class Solution:
    @classmethod
    def uniquePaths(cls, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        movements_by_x = m - 1
        movements_by_y = n - 1
        total_movemets = movements_by_x + movements_by_y

        """
        Permutation with Repetitions: How many different letter arrangements can be formed
        using the letters P E P P E R?
        In general, there are multinomial coefficients:
        n! / (n1! n2! n3! ... nr!)
        different permutations of n objects, of which n1 are alike, n2, are alike, n3 are alike,..... nr are alike.
        Therefore, the answer is 6! /(3! 2! 1!) = 60 possible arrangements of the letters P E P P E R.
        https://home.ubalt.edu/ntsbarsh/business-stat/otherapplets/comcount.htm
        """
        total_movemets_f = math.factorial(total_movemets)
        movements_by_x_f = math.factorial(movements_by_x)
        movements_by_y_f = math.factorial(movements_by_y)

        total_paths = int(total_movemets_f / movements_by_x_f / movements_by_y_f)

        return total_paths


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    assert Solution.uniquePaths(3, 7) == 28
    assert Solution.uniquePaths(3, 2) == 3
    assert Solution.uniquePaths(1, 1) == 1
    assert Solution.uniquePaths(23, 12) == 193536720
    assert Solution.uniquePaths(19, 13) == 86493225
