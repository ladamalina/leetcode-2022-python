import logging
from typing import List, Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @classmethod
    def addTwoNumbers(cls, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1p: ListNode = list1
        l2p: ListNode = list2
        over_sum: int = 0
        l3_head: Optional[ListNode] = None
        l3_tail: Optional[ListNode] = None
        while l1p is not None or l2p is not None:
            l1val: int = 0
            if l1p is not None:
                l1val = l1p.val
            l2val: int = 0
            if l2p is not None:
                l2val = l2p.val

            current_sum: int = l1val + l2val + over_sum
            if current_sum >= 10:
                over_sum = current_sum // 10
                current_sum = current_sum % 10
            else:
                over_sum = 0
            l3_head, l3_tail = Solution.append_val(l3_head, l3_tail, current_sum)
            if l1p is not None:
                l1p = l1p.next
            if l2p is not None:
                l2p = l2p.next
        if over_sum > 0:
            l3_head, l3_tail = Solution.append_val(l3_head, l3_tail, over_sum)

        return l3_head

    @classmethod
    def append_val(cls, l_head: Optional[ListNode], l_tail: Optional[ListNode], val: int) \
            -> Tuple[ListNode, ListNode]:
        new_node: ListNode = ListNode(val)
        if l_head is None:
            l_head = new_node
            l_tail = new_node
        else:
            l_tail.next = new_node
            l_tail = new_node

        return l_head, l_tail


def check_assertions(l_head: ListNode, expected_vals: List[int]) -> None:
    logging.debug(f"expected_vals={expected_vals}")
    lp = l_head
    for val in expected_vals:
        logging.debug(f"val={val}, lp.val={lp.val}")
        assert val == lp.val
        lp = lp.next
    assert lp is None
    logging.debug("." * 40)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    l1: ListNode = ListNode(2, ListNode(4, ListNode(3)))
    l2: ListNode = ListNode(5, ListNode(6, ListNode(4)))
    l3: ListNode = Solution.addTwoNumbers(l1, l2)
    expected_vals3: List[int] = [7, 0, 8]
    check_assertions(l3, expected_vals3)

    l1: ListNode = ListNode(0)
    l2: ListNode = ListNode(0)
    l3: ListNode = Solution.addTwoNumbers(l1, l2)
    expected_vals3: List[int] = [0]
    check_assertions(l3, expected_vals3)

    l1: ListNode = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2: ListNode = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    l3: ListNode = Solution.addTwoNumbers(l1, l2)
    expected_vals3: List[int] = [8, 9, 9, 9, 0, 0, 0, 1]
    check_assertions(l3, expected_vals3)
