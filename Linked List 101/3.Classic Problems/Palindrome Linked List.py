# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ListNode import *


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        tail_node = head
        mid_node = head
        while tail_node:
            tail_node = tail_node.next
            mid_node = mid_node.next.next
        prev_node = None
        while mid_node:
            next_node = mid_node.next
            mid_node.next = prev_node
            prev_node = mid_node
            mid_node = next_node


if __name__ == "__main__":
    nums = [1, 2, 2, 1]
    head = list_to_linked_list(nums)
    s = Solution()
    print(s.isPalindrome(head))
