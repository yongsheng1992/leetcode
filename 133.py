"""
    133. 克隆图
    -----------
    注意Python中的可变参数，如果不给初始值，那么所有的类都会使用缺省默认值。使用dfs和bfs都可以解决
"""
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def __init__(self):
        self.visited = [None] * 101

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        if self.visited[node.val]:
            return self.visited[node.val]

        node1 = Node(val=node.val, neighbors=[])
        self.visited[node.val] = node1

        for n in node.neighbors:
            node1.neighbors.append(self.cloneGraph(n))

        return node1
