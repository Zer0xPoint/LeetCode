# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        head = TreeNode(postorder[-1], None, None)

        def sub_tree(node, inorder_list, postorder_list):
            last_node_val = postorder_list[-1]
            left_sub_tree_vals = inorder_list[0, inorder_list.index(last_node_val)]
            right_sub_tree_vals = inorder_list[inorder_list.index(last_node_val), -1]

            if node:
                if not node.left and not node.right:
                    return node
                node.left = sub_tree()
