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
        k += 1
        while dummy_head.next:
            list_len += 1
            tail_node = tail_node.next
            dummy_head = dummy_head.next
        tail_node.next = head_node

        # for __ in range(k):
        #     head_node = head_node.next
        #     tail_node = tail_node.next
        #     print("head", head_node.val)
        #     print("tail", tail_node.val)

        # for i in range(list_len % k):
        #     for j in range(list_len - 1):
        #         tail_node = tail_node.next
        #         print("tail", tail_node.val)

        k %= list_len
        if k:
            for i in range(list_len - k + 1):
                tail_node = tail_node.next

        head_node = tail_node.next
        tail_node.next = None

        return head_node


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    nums = [0, 1, 2]
    k = 4
    head = list_to_linked_list(nums)
    s = Solution()
    traverse_linked_list(s.rotateRight(head, k))
