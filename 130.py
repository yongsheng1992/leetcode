"""
    130. 被围绕的区域
    ----------------
    从四个边界开始遍历，然后没有遍历到的'O'节点就是需要被修改的。下面的代码可以不需要flag数组，直接用board做标记。
    同时官方题解的dfs写的比下面的方式优雅的多了，值得学习。
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n == 0:
            return

        m = len(board[0])

        flag = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(m):
            if board[0][i] == 'O':
                self.dfs(0, i, n, m, flag, board)
            if board[n-1][i] == 'O':
                self.dfs(n - 1, i, n, m, flag, board)

        for i in range(n):
            if board[i][0] == 'O':
                self.dfs(i, 0, n, m, flag, board)
            if board[i][m-1] == 'O':
                self.dfs(i, m - 1, n, m, flag, board)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and not flag[i][j]:
                    board[i][j] = 'X'

    def dfs(self, x, y, n, m, flag, board):
        if flag[x][y]:
            return

        if board[x][y] != 'O':
            return

        flag[x][y] = 1

        x0, y0 = x - 1, y
        x1, y1 = x + 1, y
        x2, y2 = x, y - 1
        x3, y3 = x, y + 1

        if x0 >= 0 and board[x0][y0] == 'O':
            self.dfs(x0, y0, n, m, flag, board)

        if x1 < n and board[x1][y1] == 'O':
            self.dfs(x1, y1, n, m, flag, board)

        if y2 >= 0 and board[x2][y2] == 'O':
            self.dfs(x2, y2, n, m, flag, board)

        if y3 < m and board[x3][y3] == 'O':
            self.dfs(x3, y3, n, m, flag, board)


def test():
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    solution = Solution()
    solution.solve(board)
    for i in board:
        print(i)


if __name__ == '__main__':
    test()
