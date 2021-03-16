# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        curr_node = head
        # next_node = Node
        while curr_node:
            # next_node = curr_node.next
            copy_node = Node(curr_node.val, curr_node.next)
            curr_node.next = copy_node
            curr_node = curr_node.next

        curr_node = head
        while curr_node:
            if curr_node.random:
                curr_node.next.random = curr_node.random
            curr_node = curr_node.next.next

        curr_node = head
        dummy_head = Node(0, None)
        copy_node = dummy_head
        while curr_node:
            copy_node.next = curr_node.next
            copy_node = curr_node.next

            curr_node.next = curr_node.next.next
            curr_node = curr_node.next.next

        return dummy_head
