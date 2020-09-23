"""
    617. 合并二叉树
    --------------
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        def dfs(n1: TreeNode, n2: TreeNode):
            if not n1 and not n2:
                return None

            node = TreeNode(0)
            l1, l2 = None, None
            r1, r2 = None, None
            if n1:
                l1 = n1.left
                r1 = n1.right
                node.val += n1.val
            if n2:
                l2 = n2.left
                r2 = n2.right
                node.val += n2.val

            node.left = dfs(l1, l2)
            node.right = dfs(r1, r2)

            return node

        return dfs(t1, t2)
