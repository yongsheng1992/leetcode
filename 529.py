"""
    529. 扫雷游戏
    ------------
    是否bfs便利整个图。
"""
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click
        m = len(board)
        if m == 0:
            return board

        n = len(board[0])
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board

        self.bfs(x, y, m, n, board)
        return board

    def bfs(self, xs, ys, m, n, board):
        queue = [(xs, ys)]
        flag = [[0 for _ in range(n)] for _ in range(m)]
        while queue:
            x, y = queue.pop(0)

            direct = [
                (x - 1, y),
                (x + 1, y),
                (x, y - 1),
                (x, y + 1),
                (x - 1, y - 1),
                (x - 1, y + 1),
                (x + 1, y - 1),
                (x + 1, y + 1)
            ]
            num = 0
            for x1, y1 in direct:
                if 0 <= x1 < m and 0 <= y1 < n:
                    if board[x1][y1] == 'M':
                        num += 1
            if num != 0:
                board[x][y] = str(num)
            else:
                board[x][y] = 'B'
                for x1, y1 in direct:
                    if 0 <= x1 < m and 0 <= y1 < n:
                        if board[x1][y1] == 'E' and flag[x1][y1] == 0:
                            flag[x1][y1] = 1
                            queue.append((x1, y1))