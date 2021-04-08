# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
            
        def lca(node):
            if not node:
                return None
            if node is p or node is q:
                return node
            left_node = lca(node.left)
            right_node = lca(node.right)
            
            if left_node or right_node:
                return node
            else:
                return None
            
                    
            
