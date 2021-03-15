# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        curr_node = head
        while curr_node:
            if not curr_node.child:
                curr_node = curr_node.next
                continue
            child_node = curr_node.child
            while child_node.next:
                child_node = child_node.next
            child_node.next = curr_node.next
            if curr_node.next:
                curr_node.next.prev = child_node
            curr_node.next = curr_node.child
            curr_node.child.prev = curr_node
            curr_node.child = None
        return head

