"""
    404. 左叶子之和
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        def solve(node: TreeNode, flag):
            if not node:
                return 0
            res = 0
            if flag and not node.left and not node.right:
                res += node.val
            res += solve(node.left, 1)
            res += solve(node.right, 0)
            return res

        return solve(root, 0)
