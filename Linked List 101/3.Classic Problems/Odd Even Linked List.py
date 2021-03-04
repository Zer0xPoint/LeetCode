# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ListNode import *


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:


if __name__ == '__main__':
    nums = [1, 2, 3, 6, 4, 5, 6]
    # nums = [1]
    # val = 1
    s = Solution()
    head = list_to_linked_list(nums)
    print(traverse_linked_list(s.oddEvenList(head)))
