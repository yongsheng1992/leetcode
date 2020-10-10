"""
    199. 二叉树的右视图
    -----------------
    bfs
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        stack = []

        if not root:
            return res

        stack.append(root)
        while stack:
            res.append(stack[-1].val)

            n = len(stack)
            for i in range(n):
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return res
