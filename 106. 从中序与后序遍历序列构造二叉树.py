"""
    106. 从中序与后序遍历序列构造二叉树
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def solve(inorder: List[int], postorder: List[int]):
            if not inorder:
                return None

            root_val = postorder[-1]
            idx = inorder.index(root_val)
            root = TreeNode(root_val)

            root.left = solve(inorder[:idx], postorder[:idx])
            root.right = solve(inorder[idx + 1:], postorder[idx:-1])

            return root

        return solve(inorder, postorder)
