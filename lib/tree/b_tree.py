# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def list_to_bst(self, nums):
        if not nums:
            return None

        mid_idx = len(nums) // 2

        node = TreeNode(nums[mid_idx])
        node.left = self.list_to_bst(nums[0:mid_idx])
        node.right = self.list_to_bst(nums[mid_idx + 1:])

        return node

    def traverse_bst(self, node):
        def Traversal(node, res_list):
            if node:
                Traversal(node.left, res)
                res.append(node.val)
                Traversal(node.right, res)

        res = []
        Traversal(node, res)
        return res