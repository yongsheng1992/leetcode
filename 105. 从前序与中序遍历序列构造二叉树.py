"""
    105. 从前序与中序遍历序列构造二叉树
    --------------------------------
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def solve(idx1, idx2):
            if idx1 > idx2:
                return None

            mid = preorder.pop(0)
            idx = inorder.index(mid)
            node = TreeNode(mid)

            node.left = solve(idx1, idx-1)
            node.right = solve(idx+1, idx2)

            return node

        return solve(0, len(inorder)-1)
