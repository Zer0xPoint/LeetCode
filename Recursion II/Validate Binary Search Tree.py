# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # head = root

        def is_BST(node, low=-math.inf, high=math.inf):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False

            return is_BST(node.left, low, node.val) and is_BST(node.right, node.val, high)

        return is_BST(root)


tree = TreeNode(5, TreeNode(2), TreeNode(4, TreeNode(3), TreeNode(6)))
tree = TreeNode(2, TreeNode(1), TreeNode(3))
tree = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
print(Solution.isValidBST(Solution(), tree))
