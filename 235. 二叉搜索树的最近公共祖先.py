"""
    235. 二叉搜索树的最近公共祖先
    --------------------------
    没有看到是二叉搜索树。如果是二叉搜索树，可以一次遍历就找到分叉点
"""
from copy import deepcopy


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack_p = []
        stack_q = []

        def solve(node: TreeNode, temp):
            if not node:
                return False

            temp.append(node)

            if node.val == p.val:
                nonlocal stack_p
                stack_p = deepcopy(temp)
            elif node.val == q.val:
                nonlocal stack_q
                stack_q = deepcopy(temp)

            if stack_p and stack_q:
                return True

            if solve(node.left, temp):
                return True

            if solve(node.right, temp):
                return True

            temp.pop()
            return False

        solve(root, [])

        res = None

        for i in range(min(len(stack_q), len(stack_p))):
            if stack_p[i].val == stack_q[i].val:
                res = stack_q[i]
            else:
                break

        return res
