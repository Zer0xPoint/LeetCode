# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
#         inorder_dict = {}
#         for index, value in enumerate(inorder):
#             inorder_dict[value] = index
#
#         def sub_tree(inorder_start, inorder_end, postorder_start, postorder_end):
#             if postorder_start > postorder_end:
#                 return None
#             else:
#                 print(postorder[postorder_end])
#                 node = TreeNode(postorder[postorder_end])
#                 mid_node_index = inorder_dict[node.val]
#                 mid_node_index_delta = mid_node_index - inorder_start
#
#                 node.left = sub_tree(inorder_start, mid_node_index - 1,
#                                      postorder_start, postorder_start + mid_node_index_delta - 1)
#                 node.right = sub_tree(inorder_start + mid_node_index + 1, inorder_end,
#                                       postorder_start + mid_node_index_delta, postorder_end - 1)
#                 return node
#
#         return sub_tree(0, len(inorder) - 1, 0, len(postorder) - 1)

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorder_index_dict = {}
        for index, value in enumerate(inorder):
            inorder_index_dict[value] = index

        def sub_tree(in_start, in_end, post_start, post_end):
            if post_start <= post_end:
                node = TreeNode(postorder[post_end])
                in_root_index = inorder_index_dict[node.val]
                in_index_delta = in_root_index - in_start
                node.left = sub_tree(in_start, in_root_index - 1,
                                     post_start, post_start + in_index_delta - 1)
                node.right = sub_tree(in_start + in_index_delta + 1, in_end,
                                      post_start + in_index_delta, post_end - 1)
                return node
            else:
                return None

        return sub_tree(0, len(inorder) - 1, 0, len(postorder) - 1)


if __name__ == "__main__":
    s = Solution()
    inorder_list = [9, 3, 15, 20, 7]
    postorder_list = [9, 15, 7, 20, 3]

    tree = s.buildTree(inorder_list, postorder_list)
    print(tree.left.val)
