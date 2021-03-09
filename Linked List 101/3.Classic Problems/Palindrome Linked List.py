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
            if tail_node.next is None:
                break
            tail_node = tail_node.next.next
            mid_node = mid_node.next
        node = None
        while mid_node:
            next_node = mid_node.next
            mid_node.next = node
            node = mid_node
            mid_node = next_node
        while node and head:
            if node.val is not head.val:
                return False
            node = node.next
            head = head.next
        return True


if __name__ == "__main__":
    nums = [1, 2, 3, 3, 2, 1]
    head = list_to_linked_list(nums)
    s = Solution()
    print(s.isPalindrome(head))
