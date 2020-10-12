"""
    530. 二叉搜索树的最小绝对差
    -------------------------
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        ans = 1000000
        p = -1

        def solve(node):
            if not node:
                return
            solve(node.left)
            nonlocal p
            nonlocal ans
            if p != -1:
                ans = min(node.val - p, ans)
            p = node.val
            solve(node.right)

        solve(root)

        return ans
