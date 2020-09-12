"""
    面试题 08.12. 八皇后
    -------------------
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = [-1] * n
        cols = set()
        diagonal1 = set()
        diagonal2 = set()
        res = []
        rows = ['.'] * n

        def get_board():
            board = []
            for i in range(n):
                rows[queens[i]] = 'Q'
                board.append(''.join(rows))
                rows[queens[i]] = '.'
            res.append(board)

        def solve(row):
            if row == n:
                get_board()
                return
            for i in range(n):
                if i in cols or row - i in diagonal1 or row + i in diagonal2:
                    continue
                queens[row] = i
                cols.add(i)
                diagonal1.add(row-i)
                diagonal2.add(row+i)
                solve(row+1)
                cols.remove(i)
                diagonal1.remove(row-i)
                diagonal2.remove(row+i)

        solve(0)
        return res
