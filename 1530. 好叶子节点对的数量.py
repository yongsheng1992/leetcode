"""
    1530. 好叶子节点对的数量
    ----------------------
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = 0

        def solve(node: TreeNode):
            if not node:
                return []

            if not node.left and not node.right:
                return [1]

            l = solve(node.left)
            r = solve(node.right)

            for i in l:
                for j in r:
                    if i + j <= distance:
                        nonlocal ans
                        ans += 1

            depth = []
            for i in l + r:
                if i + 1 <= distance:
                    depth.append(i+1)

            return depth

        solve(root)

        return ans


