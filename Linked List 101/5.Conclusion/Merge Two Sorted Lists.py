# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from lib.linked_list.linked_list import *


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        sorted_head_node = dummy_head
        while l1 and l2:
            if l1.val <= l2.val:
                sorted_head_node.next = l1
                l1 = l1.next
            else:
                sorted_head_node.next = l2
                l2 = l2.next
            sorted_head_node = sorted_head_node.next
        sorted_head_node.next = l1 if l2 is None else l2
        return dummy_head.next


if __name__ == '__main__':
    s = Solution()
    l1 = [1, 2, 4]
    l2 = [3, 4, 5]
    l1_head = list_to_linked_list(l1)
    l2_head = list_to_linked_list(l2)
    traverse_linked_list(s.mergeTwoLists(l1_head, l2_head))
