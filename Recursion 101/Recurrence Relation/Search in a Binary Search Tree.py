# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # while root and root.val is not val:
        #     root = root.left if root.val > val else root.right
        # return root
        if not root or root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
        # return self.searchBST(root.right if root.val < val else root.left, val)
