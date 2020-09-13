"""
    212. 单词搜索 II
    ---------------
    对words构建字典树，然后再遍历board查找单词是否出现在字典树中
"""
from typing import List


class TreeNode:

    def __init__(self, value=None):
        self.is_leaf = False
        self.value = None
        self.children = {}
        self.fail = None


class TrieTree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TreeNode()
            node = node.children[char]
        node.is_leaf = True
        node.value = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        if not n:
            return []
        m = len(board[0])
        trie = TrieTree()
        visited = [[0 for _ in range(m)] for _ in range(n)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = set()

        def build(x, y, node: TreeNode):
            if visited[x][y]:
                return

            if node.is_leaf and node.value not in res:
                res.add(node.value)

            visited[x][y] = 1
            for x0, y0 in directions:
                x1, y1 = x + x0, y + y0
                if 0 <= x1 < n and 0 <= y1 < m and not visited[x1][y1]:
                    char = board[x1][y1]
                    if char in node.children:
                        build(x1, y1, node.children[char])

            visited[x][y] = 0

        for word in words:
            trie.insert(word)

        for i in range(n):
            for j in range(m):
                if board[i][j] in trie.root.children:
                    build(i, j, trie.root.children[board[i][j]])

        return list(res)
