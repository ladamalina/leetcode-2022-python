import logging
import math
from typing import List


class NumArray:
    MIN_CHUNK_SIZE: int = 3

    def __init__(self, nums: List[int]):
        self._nums: List[int] = nums

        chunk_size_sqrt: int = math.ceil(math.sqrt(len(self._nums)))
        self._chunk_size = max(chunk_size_sqrt, NumArray.MIN_CHUNK_SIZE)

        chunks_total: int = math.ceil(len(self._nums) / self._chunk_size)
        self._chunk_to_sum: List[int] = [0] * chunks_total

        for current_chunk in range(chunks_total):
            begin_i: int = current_chunk * self._chunk_size
            end_i: int = min(begin_i + self._chunk_size - 1, len(self._nums) - 1)
            chunk_sum: int = 0
            for i in range(begin_i, end_i + 1):
                chunk_sum += self._nums[i]
            self._chunk_to_sum[current_chunk] = chunk_sum

    def update(self, index: int, val: int) -> None:
        old_val: int = self._nums[index]
        if old_val == val:
            return

        chunk_num: int = index // self._chunk_size
        chunk_sum: int = self._chunk_to_sum[chunk_num] - old_val + val
        self._chunk_to_sum[chunk_num] = chunk_sum
        self._nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        left_chunk: int = left // self._chunk_size
        right_chunk: int = right // self._chunk_size

        chunk_sum: int = 0
        for chunk_num in range(left_chunk, right_chunk + 1):
            chunk_sum += self._chunk_to_sum[chunk_num]

        # remove left redundant nums
        left_chunk_begin_i: int = left_chunk * self._chunk_size
        for i in range(left_chunk_begin_i, left):
            chunk_sum -= self._nums[i]

        # remove right redundant nums
        right_chunk_end_i: int = min(right_chunk * self._chunk_size + self._chunk_size - 1,
                                     len(self._nums) - 1)
        for i in range(right + 1, right_chunk_end_i + 1):
            chunk_sum -= self._nums[i]

        return chunk_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    num_array1 = NumArray([1, 3, 5])
    assert num_array1.sumRange(0, 2) == 9
    num_array1.update(1, 2)
    assert num_array1.sumRange(0, 2) == 8

    num_array2 = NumArray([5, 18, 13])
    assert num_array2.sumRange(0, 2) == 36
    num_array2.update(1, -1)
    num_array2.update(2, 3)
    num_array2.update(0, 5)
    num_array2.update(0, -4)
    assert num_array2.sumRange(0, 2) == -2

    num_array3 = NumArray([9, -8])
    logging.debug(f"num_array3._nums = {num_array3._nums}")
    logging.debug(f"num_array3._chunk_size = {num_array3._chunk_size}")
    logging.debug(f"num_array3._chunk_to_sum = {num_array3._chunk_to_sum}")
    num_array3.update(0, 3)
    logging.debug(f"num_array3._nums = {num_array3._nums}")
    logging.debug(f"num_array3._chunk_size = {num_array3._chunk_size}")
    logging.debug(f"num_array3._chunk_to_sum = {num_array3._chunk_to_sum}")
    assert num_array3.sumRange(1, 1) == -8
    assert num_array3.sumRange(0, 1) == -5
    num_array3.update(1, -3)
    assert num_array3.sumRange(0, 1) == 0
