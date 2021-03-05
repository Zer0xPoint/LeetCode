# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ListNode import *


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head:
            odd_index_node = head
            even_index_node = head.next
            even_head_node = even_index_node
            # even_head_node.next = even_index_node

            while even_index_node and even_index_node.next:
                odd_index_node.next = odd_index_node.next.next
                even_index_node.next = even_index_node.next.next
                odd_index_node = odd_index_node.next
                even_index_node = even_index_node.next

            odd_index_node.next = even_head_node

        return head


if __name__ == '__main__':
    nums = [1, 2, 3, 6, 4, 5, 6]
    # nums = [1, 2, 3, 4, 5]
    nums = [1]
    # val = 1
    s = Solution()
    head = list_to_linked_list(nums)
    print(traverse_linked_list(s.oddEvenList(head)))
