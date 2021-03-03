from ListNode import *


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        black_node = head
        dummy_node = black_node
        head_node = ListNode
        head_node.next = black_node
        while black_node.next:
            dummy_node = black_node.next
            black_node.next = black_node.next.next
            # head_node.next = dummy_node
            dummy_node.next = head_node.next
            head_node.next = dummy_node

        return dummy_node


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    # nums = [23, 6, 15]
    # nums = [1]
    nums = []
    head = list_to_linked_list(nums)
    s = Solution()
    traverse_linked_list(s.reverseList(head))
