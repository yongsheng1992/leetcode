class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (not p and q) or (p and not q):
            return False

        if not p and not q:
            return True

        if not p.val == q.val:
            return False

        if not self.isSameTree(p.left, q.left):
            return False

        if not self.isSameTree(p.right, q.right):
            return False

        return True
