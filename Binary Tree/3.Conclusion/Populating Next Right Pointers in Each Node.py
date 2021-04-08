# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr_level = [root]
        while root and curr_level:
            curr_nodes = []
            next_level = []
            for node in curr_level:
                curr_nodes.append(node)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                    
            for i in range(0, len(curr_nodes) - 1):
                curr_nodes[i].next = curr_nodes[i + 1]
            curr_level = next_level

        return root


if __name__ == "__main__":
    s = Solution()
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6, Node(7))))
    connect_tree = s.connect(tree)
    print(connect_tree)
