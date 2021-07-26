# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid_idx = len(nums) // 2

        node = TreeNode(nums[mid_idx])
        node.left = self.sortedArrayToBST(nums[0:mid_idx])
        node.right = self.sortedArrayToBST(nums[mid_idx + 1:])

        return node


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    s = Solution()
    s.sortedArrayToBST(nums)
