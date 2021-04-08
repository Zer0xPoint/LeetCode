# Definition for a Node.
class Node:
    def __init__(self,
                 val: int=0,
                 left: 'Node'=None,
                 right: 'Node'=None,
                 next: 'Node'=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        node = root

        #new (parent) level
        while node:
            #creating a dummy leftmost node for the next (child) level
            curr = dummy = Node()
            #while nodes exist at the same (ie parent) level
            while node:
                if node.left:
                    curr.next = node.left
                    curr = curr.next
                if node.right:
                    curr.next = node.right
                    curr = curr.next
                node = node.next
            #no more nodes at this (parent) level, dropping to next (child) level
            node = dummy.next

        return root


if __name__ == "__main__":
    s = Solution()
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6, Node(7))))
    connect_tree = s.connect(tree)
    print(connect_tree)

