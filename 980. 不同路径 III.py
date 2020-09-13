"""
    980. 不同路径 III
    ----------------
"""
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0

        m = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        res = 0
        total = 0

        def dfs(x, y, path):
            if grid[x][y] == 2:
                if path - 1 == total:
                    nonlocal res
                    res += 1
                return

            grid[x][y] = -1
            for x0, y0 in directions:
                x1, y1 = x + x0, y + y0
                if 0 <= x1 < n and 0 <= y1 < m and grid[x1][y1] >= 0:
                    dfs(x1, y1, path+1)

            grid[x][y] = 0

        x, y = 0, 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    x, y = i, j
                elif grid[i][j] == 0:
                    total += 1
        dfs(x, y, 0)
        for i in grid:
            print(i)
        return res
