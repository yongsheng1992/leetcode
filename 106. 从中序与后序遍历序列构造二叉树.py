"""
    106. 从中序与后序遍历序列构造二叉树
    --------------------------------
    优化空间和时间
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def solve(idx1, idx2):
            if idx1 > idx2:
                return None

            mid = postorder.pop()
            idx = inorder.index(mid)
            node = TreeNode(mid)

            node.right = solve(idx + 1, idx2)
            node.left = solve(idx1, idx-1)

            return node

        return solve(0, len(inorder)-1)
