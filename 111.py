"""
    111. 二叉树的最小深度
    --------------------
    使用dfs遍历即可
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.dfs(root, 1)

    def dfs(self, root, depth):
        d1, d2 = None, None
        if root.left:
            d1 = self.dfs(root.left, depth+1)
        if root.right:
            d2 = self.dfs(root.right, depth+1)

        if d1 and d2:
            return min(d1, d2)

        if d1 and not d2:
            return d1

        if d2 and not d1:
            return d2

        if not d1 and not d2:
            return depth
