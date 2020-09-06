"""
    107. 二叉树的层次遍历 II
    -----------------------
    简单的便利二叉树
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        def dfs(node: TreeNode, level: int):
            if not node:
                return

            dfs(node.left, level+1)
            dfs(node.right, level+1)

            nonlocal res
            if level >= len(res):
                for _ in range(level - len(res) + 1):
                    res.append([])
            res[level].append(node.val)
        dfs(root, 0)
        res.reverse()
        return res
