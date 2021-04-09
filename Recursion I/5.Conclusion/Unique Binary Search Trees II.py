class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate(i,j):
            if j-i < 0:
                return [None]
            elif j-i == 0:
                return [TreeNode(i)]
            else:
                res = []
                for k in range(i,j+1):
                    left = generate(i,k-1)
                    right = generate(k+1,j)
                    for l in left:
                        for r in right:
                            root = TreeNode(k)
                            root.left = l
                            root.right = r
                            res.append(root)
                return res
        if n == 0:
            return []
        else:
            return generate(1,n)