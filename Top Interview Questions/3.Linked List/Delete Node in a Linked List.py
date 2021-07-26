# Definition for singly-linked list.
from lib.linked_list.linked_list import list_to_linked_list


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    delete_node = 3
    head_node = list_to_linked_list(nums)

    s = Solution()
    s.deleteNode()