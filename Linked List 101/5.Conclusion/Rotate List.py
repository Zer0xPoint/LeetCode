# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from lib.linked_list.linked_list import *


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        dummy_head = head
        head_node = tail_node = head
        list_len = 1
        while dummy_head.next:
            list_len += 1
            tail_node = tail_node.next
            dummy_head = dummy_head.next
        tail_node.next = head_node

        for __ in range(k):
            head_node = head_node.next
            tail_node = tail_node.next
            print("head", head_node.val)
            print("tail", tail_node.val)

        tail_node.next = None

        return dummy_head
        # for __ in range(list_len):


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    k = 3
    head = list_to_linked_list(nums)
    s = Solution()
    traverse_linked_list(s.rotateRight(head, k))
