"""
    110. 平衡二叉树
    --------------
    使用dfs遍历树，在遍历的时候需要不断的判断左右子树的高度是否超过2
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        _, flag = self.dfs(root, 0)
        return flag

    def dfs(self, root, h):
        if not root:
            return h, True

        l, flag1 = self.dfs(root.left, h+1)
        if not flag1:
            return l, flag1

        r, flag2 = self.dfs(root.right, h+1)
        if not flag2:
            return r, flag2

        flag = flag1 & flag2
        if abs(l-r) >= 2:
            flag &= False

        return max(l, r), flag
