"""
    257. 二叉树的所有路径
    -------------------
    简单的dfs。
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []

        def dfs(node, path):
            if not node:
                return
            path = path + [str(node.val)]
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)

            if not node.left and not node.right:
                res.append('->'.join(path))

        dfs(root, [])
        return res
