# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ListNode import *


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # if not head:
        #     return head
        dummy_node = ListNode
        dummy_node.next = head
        second_node = dummy_node
        first_node = dummy_node.next
        while first_node:
            if first_node.val is val:
                second_node.next = second_node.next.next
            else:
                second_node = second_node.next
            first_node = first_node.next
        return dummy_node.next


if __name__ == '__main__':
    nums = [1, 2, 3, 6, 4, 5, 6]
    nums = [1]
    val = 1
    s = Solution()
    head = list_to_linked_list(nums)
    print(traverse_linked_list(s.removeElements(head, val)))
