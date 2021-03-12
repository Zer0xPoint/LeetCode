# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from lib.linked_list.linked_list import *


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # two pointer, one for curr, another for next
        dummy_head = ListNode
        curr_node = ListNode(0)
        next_node = ListNode(0)
        dummy_head.next = curr_node
        curr_node.next = next_node

        while l1 or l2:
            curr_val = 0
            if l1:
                curr_val += l1.val
                l1 = l1.next
            if l2:
                curr_val += l2.val
                l2 = l2.next

            if curr_val < 9:
                curr_node.val += curr_val
                next_node = ListNode(0)
            else:
                curr_node.val += curr_val - 10
                next_node = ListNode(1)

            curr_node.next = next_node
            curr_node = curr_node.next

        return dummy_head.next


if __name__ == '__main__':
    s = Solution()
    l1 = [9, 9, 9]
    l2 = [2]

    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    l1_head = list_to_linked_list(l1)
    l2_head = list_to_linked_list(l2)
    traverse_linked_list(s.addTwoNumbers(l1_head, l2_head))
