"""
    52. N皇后 II
    ------------
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        queens = [-1] * n
        cols = set()
        diagonal1 = set()
        diagonal2 = set()
        res = 0

        def solve(row):
            if row == n:
                nonlocal res
                res += 1
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
