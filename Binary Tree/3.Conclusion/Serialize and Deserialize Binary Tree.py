# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        # pre order traversal b_tree
        pre_list = []
        in_list = []
        pre_head = root
        in_head = root

        def pre_order_traversal(node):
            if not node:
                return None
            pre_list.append(node.val)
            pre_order_traversal(node.left)
            pre_order_traversal(node.right)

        pre_order_traversal(pre_head)

        def in_order_traversal(node):
            if not node:
                return None
            in_order_traversal(node.left)
            in_list.append(node.val)
            in_order_traversal(node.right)

        in_order_traversal(in_head)

        return pre_list + in_list

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        pre_list = data[:len(data) // 2]
        in_list = data[(len(data) // 2):]

        in_dict = {}
        for index, value in enumerate(in_list):
            in_dict[value] = index

        def subtree(pre_start, pre_end, in_start, in_end):
            if pre_start >= pre_end:
                return None
            else:
                print(pre_list[pre_start: pre_end], "pre")
                print(in_list[in_start: in_end], "in")
                node = TreeNode(pre_list[pre_start])
                node_index_in = in_dict[node.val]
                left_side_nodes_count = node_index_in - in_start
                node.left = subtree(pre_start + 1, pre_start + left_side_nodes_count + 1,
                                    in_start, in_start + left_side_nodes_count)
                node.right = subtree(pre_start + left_side_nodes_count + 1, pre_end,
                                     in_start + left_side_nodes_count + 1, in_end)
                return node

        root = subtree(0, len(pre_list), 0, len(in_list))
        return root


# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
# print(ser.serialize(root))
data = ser.serialize(root)
# [2, 1, 3, 2, 3, 1]
print(data)
head = deser.deserialize(data)
print(head)
# ans = deser.deserialize(ser.serialize(root))
