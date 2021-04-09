# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from lib.linked_list.linked_list import *


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head_node = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(new_head_node)
        return head
