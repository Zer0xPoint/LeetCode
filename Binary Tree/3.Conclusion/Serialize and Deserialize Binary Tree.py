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
        post_list = []
        pre_head = root
        post_head = root

        def pre_order_traversal(node):
            if not node:
                return None
            pre_order_traversal(node.left)
            pre_list.append(node.val)
            pre_order_traversal(node.right)

        pre_order_traversal(pre_head)

        def post_order_traversal(node):
            if not node:
                return None
            post_order_traversal(node.left)
            post_order_traversal(node.right)
            post_list.append(node.val)

        post_order_traversal(post_head)

        return pre_list + post_list

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """


# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(ser.serialize(root))
# ans = deser.deserialize(ser.serialize(root))
