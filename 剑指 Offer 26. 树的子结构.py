"""
    剑指 Offer 26. 树的子结构
    ------------------------
    先写出两个树是不是相同的代码，然后在以此遍历A，从当前结点开始比较。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        ans = False

        if not B:
            return ans

        def solve(n1: TreeNode, n2: TreeNode):
            if not n1 and n2:
                return False

            if (n1 and not n2) or (not n1 and not n2):
                return True

            return n1.val == n2.val and solve(n1.left, n2.left) and solve(n1.right, n2.right)

        def traverse(n: TreeNode):
            nonlocal ans
            if ans:
                return

            if not n:
                return

            if n.val == B.val and solve(n, B):
                ans = True
                return

            traverse(n.left)
            traverse(n.right)

        traverse(A)

        return ans
