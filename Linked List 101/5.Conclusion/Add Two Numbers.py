# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from lib.linked_list.linked_list import *


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        l1_node = l1
        l2_node = l2
        curr_node = dummy_head
        carry = 0
        while l1_node or l2_node:
            l1_val = l1_node.val if l1_node else 0
            l2_val = l2_node.val if l2_node else 0
            curr_val = l1_val + l2_val + carry
            carry = curr_val // 10
            curr_node.next = ListNode(curr_val % 10)
            curr_node = curr_node.next
            if l1_node:
                l1_node = l1_node.next
            if l2_node:
                l2_node = l2_node.next

        if carry:
            curr_node.next = ListNode(carry)

        return dummy_head.next


if __name__ == '__main__':
    s = Solution()
    # l1 = [9, 9, 9]
    # l2 = [2]

    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    l1_head = list_to_linked_list(l1)
    l2_head = list_to_linked_list(l2)
    traverse_linked_list(s.addTwoNumbers(l1_head, l2_head))
