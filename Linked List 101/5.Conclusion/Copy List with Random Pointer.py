# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        curr_node = head
        while curr_node:
            copy_node = Node(curr_node.val, curr_node.next)
            curr_node.next = copy_node
            curr_node = copy_node.next

        curr_node = head
        while curr_node:
            curr_node.next.random = curr_node.random and curr_node.random.next
            curr_node = curr_node.next.next

        curr_node = head
        copy_node = head_copy = head and head.next
        # print(head and head.next)
        while curr_node:
            curr_node.next = curr_node = copy_node.next
            copy_node.next = copy_node = curr_node and curr_node.next

        return head_copy
