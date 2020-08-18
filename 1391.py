"""
    1391. 检查网格中是否存在有效路径
    ------------------------------
    直接从(0,0)开始进行dfs，看是否能够到达(m-1,n-1)。
    下面的代码36到70行的判断条件可以简化。
"""
from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        if m == 0:
            return True
        n = len(grid[0])

        flag = [[False for _ in range(n)] for _ in range(m)]
        return self.dfs(0, 0, m, n, grid, flag)

    def dfs(self, x, y, m, n, g, flag):
        print(x, y)
        if flag[x][y]:
            return False

        flag[x][y] = True
        if x == m - 1 and y == n - 1:
            return True

        # 分别是上下左右
        x0, y0 = x-1, y
        x1, y1 = x+1, y
        x2, y2 = x, y-1
        x3, y3 = x, y+1

        ans = False
        if g[x][y] == 1:
            if 0 <= x2 < m and 0 <= y2 < n and g[x2][y2] in {1, 4, 6}:
                ans |= self.dfs(x2, y2, m, n, g, flag)
            if 0 <= x3 < m and 0 <= y3 < n and g[x3][y3] in {1, 3, 5}:
                ans |= self.dfs(x3, y3, m, n, g, flag)

        if g[x][y] == 2:
            if 0 <= x0 < m and 0 <= y0 < n and g[x0][y0] in {2, 3, 4}:
                ans |= self.dfs(x0, y0, m, n, g, flag)
            if 0 <= x1 < m and 0 <= y1 < n and g[x1][y1] in {2, 5, 6}:
                ans |= self.dfs(x1, y1, m, n, g, flag)

        if g[x][y] == 3:
            if 0 <= x1 < m and 0 <= y1 < n and g[x1][y1] in {2, 5, 6}:
                ans |= self.dfs(x1, y1, m, n, g, flag)
            if 0 <= x2 < m and 0 <= y2 < n and g[x2][y2] in {1, 4, 6}:
                ans |= self.dfs(x2, y2, m, n, g, flag)

        if g[x][y] == 4:
            if 0 <= x1 < m and 0 <= y1 < n and g[x1][y1] in {2, 5, 6}:
                ans |= self.dfs(x1, y1, m, n, g, flag)
            if 0 <= x3 < m and 0 <= y3 < n and g[x3][y3] in {1, 3, 5}:
                ans |= self.dfs(x3, y3, m, n, g, flag)

        if g[x][y] == 5:
            if 0 <= x0 < m and 0 <= y0 < n and g[x0][y0] in {2, 3, 4}:
                ans |= self.dfs(x0, y0, m, n, g, flag)
            if 0 <= x2 < m and 0 <= y2 < n and g[x2][y2] in {1, 4, 6}:
                ans |= self.dfs(x2, y2, m, n, g, flag)

        if g[x][y] == 6:
            if 0 <= x0 < m and 0 <= y0 < n and g[x0][y0] in {2, 3, 4}:
                ans |= self.dfs(x0, y0, m, n, g, flag)
            if 0 <= x3 < m and 0 <= y3 < n and g[x3][y3] in {1, 3, 5}:
                ans |= self.dfs(x3, y3, m, n, g, flag)

        return ans
