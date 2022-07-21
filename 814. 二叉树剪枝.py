from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        flag = self.solve(root, root.left, root.right)
        if flag:
            return None
        return root

    def solve(self, fa, left, right) -> bool:
        if fa is None:
            return True

        l = True if left is None else self.solve(left, left.left, left.right)
        r = True if right is None else self.solve(right, right.left, right.right)

        if l:
            fa.left = None
        if r:
            fa.right = None

        return fa.val == 0 and l and r
