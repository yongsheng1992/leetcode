"""
    337. 打家劫舍 III
    ----------------
    不同于198. 打家劫舍和213. 打家劫舍 II中的房间形状，本地中房间的组成二叉树，第一个房间是这个二叉树的根。解法和前面的题目
    类似，这不过是需要在二叉树山遍历。
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.dfs(root))

    def dfs(self, root: TreeNode):
        if not root:
            return 0, 0

        a, b = self.dfs(root.left)
        c, d = self.dfs(root.right)
        g = root.val
        e, f = b + d + g, max(a + c, a + d, b + c, b + d)
        return e, f
