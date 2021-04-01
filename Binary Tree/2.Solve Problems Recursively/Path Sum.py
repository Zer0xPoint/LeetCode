# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        def rec_path_sum(node, target_sum):
            if node:
                if not node.left and not node.right and target_sum == node.val:
                    return True
                return rec_path_sum(node.left, target_sum - node.val) or rec_path_sum(node.right, target_sum - node.val)

        return True if rec_path_sum(root, targetSum) else False

    # [5,4,8,11,null,13,4,7,2,null,null,null,1]


if __name__ == "__main__":
    tn = TreeNode(1, TreeNode(2, None, None), TreeNode(3, TreeNode(1, None, None), None))
    s = Solution()
    print(s.hasPathSum(tn, 4))
