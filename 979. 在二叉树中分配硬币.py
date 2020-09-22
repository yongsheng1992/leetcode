"""
    979. 在二叉树中分配硬币
    ---------------------
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node: TreeNode):
            if not node:
                return 0

            ln = dfs(node.left)
            rn = dfs(node.right)
            n = ln + rn + node.val - 1
            nonlocal ans
            ans += abs(n)
            return n

        dfs(root)
        return ans
