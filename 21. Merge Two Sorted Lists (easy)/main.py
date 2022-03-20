import logging
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @classmethod
    def mergeTwoLists(cls, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        head_node = None
        tail_node = None
        l1ptr = list1
        l2ptr = list2
        while l1ptr is not None and l2ptr is not None:
            if l1ptr.val <= l2ptr.val:
                new_node = ListNode(l1ptr.val)
                l1ptr = l1ptr.next
            else:
                new_node = ListNode(l2ptr.val)
                l2ptr = l2ptr.next
            if head_node is None:
                head_node = new_node
                tail_node = new_node
            else:
                tail_node.next = new_node
                tail_node = new_node
        if l1ptr is not None:
            tail_node.next = l1ptr
        if l2ptr is not None:
            tail_node.next = l2ptr

        return head_node


def check_assertion(list_node: ListNode, expected_vals: List[int]):
    logging.debug(f"check_assertion: expected_vals = {expected_vals}")
    current_node_ptr = list_node
    for expected_val in expected_vals:
        logging.debug(f"check_assertion: expected_val = {expected_val}, current_val = {current_node_ptr.val}")
        assert expected_val == current_node_ptr.val
        current_node_ptr = current_node_ptr.next
    assert current_node_ptr is None


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = Solution.mergeTwoLists(l1, l2)
    check_assertion(l3, [1, 1, 2, 3, 4, 4])

    l1 = None
    l2 = None
    l3 = Solution.mergeTwoLists(l1, l2)
    check_assertion(l3, [])

    l1 = None
    l2 = ListNode(0)
    l3 = Solution.mergeTwoLists(l1, l2)
    check_assertion(l3, [0])
