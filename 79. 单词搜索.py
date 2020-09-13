"""
    79. 单词搜索
    -----------
    简单的回溯
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        if n == 0:
            return False

        m = len(board[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(x, y):
            return 0 <= x < n and 0 <= y < m and (x, y) not in visited

        def solve(x, y, word):
            if not word:
                return True
            visited.add((x,y))

            for x0, y0 in directions:
                x1, y1 = x + x0, y + y0
                if check(x1, y1) and board[x1][y1] == word[0]:
                    if solve(x1, y1, word[1:]):
                        return True
            visited.remove((x, y))
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if solve(i, j, word[1:]):
                        return True
        return False
