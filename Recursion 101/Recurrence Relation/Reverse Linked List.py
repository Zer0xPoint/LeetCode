# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from lib.linked_list.linked_list import *


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr_node = head
        prev_node = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        return prev_node


nums = [1, 2, 3, 4, 5]
head = list_to_linked_list(nums)
print(head)
s = Solution
traverse_linked_list(s.reverseList(s, head))
