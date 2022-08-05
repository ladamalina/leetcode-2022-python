import logging
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @classmethod
    def deleteDuplicates(cls, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        current_node: ListNode = head
        next_node: Optional[ListNode] = current_node.next
        while next_node is not None:
            if current_node.val == next_node.val:
                current_node.next = next_node.next
                next_node = next_node.next
            else:
                current_node = next_node
                next_node = next_node.next

        return head


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    l1: ListNode = ListNode(1, ListNode(1, ListNode(2)))
    exp1: List[int] = [1, 2]
    l1_res: Optional[ListNode] = Solution.deleteDuplicates(l1)
    for e in exp1:
        assert e == l1_res.val
        l1_res = l1_res.next

    l1: ListNode = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    exp1: List[int] = [1, 2, 3]
    l1_res: Optional[ListNode] = Solution.deleteDuplicates(l1)
    for e in exp1:
        assert e == l1_res.val
        l1_res = l1_res.next

    l1: ListNode = ListNode(1, ListNode(1))
    exp1: List[int] = [1]
    l1_res: Optional[ListNode] = Solution.deleteDuplicates(l1)
    for e in exp1:
        assert e == l1_res.val
        l1_res = l1_res.next

    l1: ListNode = ListNode(1)
    exp1: List[int] = [1]
    l1_res: Optional[ListNode] = Solution.deleteDuplicates(l1)
    for e in exp1:
        assert e == l1_res.val
        l1_res = l1_res.next

    l1: ListNode = ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1)))))
    exp1: List[int] = [1]
    l1_res: Optional[ListNode] = Solution.deleteDuplicates(l1)
    for e in exp1:
        assert e == l1_res.val
        l1_res = l1_res.next

    l1: ListNode = None
    l1_res: Optional[ListNode] = Solution.deleteDuplicates(l1)
    assert l1_res is None
