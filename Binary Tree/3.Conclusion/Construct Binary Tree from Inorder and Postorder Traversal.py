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

        inorder_dict = {}
        for index, value in enumerate(inorder):
            inorder_dict[value] = index

        def sub_tree(node, inorder_list, postorder_list):
            pass

        return head


if __name__ == "__main__":
    s = Solution()
    inorder_list = [3, 1, 2]
    postorder_list = [3, 2, 1]
    s.buildTree(inorder_list, postorder_list)
