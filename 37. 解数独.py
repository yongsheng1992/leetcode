"""
    37. 解数独
    ----------
    回溯
"""
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(m)]
        grid = [set() for _ in range(n)]
        spaces = []

        def solve(idx):

            if idx == len(spaces):
                return True

            x, y = spaces[idx]
            grid_no = (x // 3) * 3 + y // 3

            for i in range(1, 10):
                i = str(i)
                if i in rows[x] or i in cols[y] or i in grid[grid_no]:
                    continue

                rows[x].add(i)
                cols[y].add(i)
                grid[grid_no].add(i)
                board[x][y] = i

                if solve(idx + 1):
                    return True

                board[x][y] = '.'
                rows[x].remove(i)
                cols[y].remove(i)
                grid[grid_no].remove(i)

            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] != '.':
                    grid_no = (i // 3) * 3 + j // 3
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    grid[grid_no].add(board[i][j])
                else:
                    spaces.append((i, j))

        solve(0)
