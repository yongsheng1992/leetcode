"""
    98. 验证二叉搜索树
    -----------------
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def in_order(node: TreeNode, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            if node.val >= upper or node.val <= lower:
                return False

            if not in_order(node.left, lower, node.val):
                return False

            if not in_order(node.right, node.val, upper):
                return False

            return True

        ans = in_order(root)
        return ans


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)

    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(20)

    solution = Solution()
    print(solution.isValidBST(root))
