from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_index_dict = {}
        for index, value in enumerate(inorder):
            inorder_index_dict[value] = index

        def sub_tree(in_start, in_end, pre_start, pre_end):
            if pre_start <= pre_end:
                node = TreeNode(preorder[pre_start])
                in_root_index = inorder_index_dict[node.val]
                in_index_delta = in_root_index - in_start
                node.left = sub_tree(in_start, in_root_index - 1,
                                     pre_start + 1, pre_start + in_index_delta)
                node.right = sub_tree(in_start + in_index_delta + 1, in_end,
                                      pre_start + in_index_delta + 1, pre_end)
                return node
            else:
                return None

        return sub_tree(0, len(preorder) - 1, 0, len(inorder) - 1)


if __name__ == "__main__":
    s = Solution()
    inorder_list = [9, 3, 15, 20, 7]
    preorder_list = [3, 9, 20, 15, 7]

    tree = s.buildTree(preorder_list, inorder_list)
    print(tree.left.val)
