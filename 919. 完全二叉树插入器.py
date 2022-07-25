from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.nodes = []
        self.root = root
        if root is not None:
            queue = [root]
            while queue:
                node = queue.pop(0)
                self.nodes.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    def insert(self, val: int) -> int:
        self.nodes.append(TreeNode(val))
        idx = len(self.nodes)
        fa = self.nodes[idx // 2 - 1]
        if idx % 2 == 0:
            fa.left = self.nodes[idx-1]
        else:
            fa.right = self.nodes[idx-1]
        return fa.val

    def get_root(self) -> TreeNode:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()

if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    cbt = CBTInserter(tree)
    cbt.insert(3)
    cbt.insert(4)
    cbt.get_root()
    print(tree.left.left.val)

