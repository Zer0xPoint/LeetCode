# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def Traversal(node, res_list):
            if node:
                Traversal(node.left, res)
                Traversal(node.right, res)
                res.append(node.val)

        res = []
        Traversal(root, res)
        return res
