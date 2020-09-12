"""
    1001. 网格照明
    -------------
    用简单的模拟会超时。使用4个字段保存灯亮的信息，这里借鉴8皇后判断是否可以摆放皇后的思路。
    矩阵式稀疏的，用数组会爆内存。
"""
from typing import List


class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        grid = {}
        rows = {}
        cols = {}
        d1 = {}
        d2 = {}
        res = [0] * len(queries)

        for x, y in lamps:
            grid.setdefault(x, {})
            grid[x][y] = 1
            rows.setdefault(x, 0)
            cols.setdefault(y, 0)
            d1.setdefault(x+y, 0)
            d2.setdefault(x+N-y-1, 0)
            rows[x] += 1
            cols[y] += 1
            d1[x+y] += 1
            d2[x+N-y-1] += 1


        def switch(x, y, flag):
            grid[x].pop(y)
            rows[x] += flag
            cols[y] += flag
            d1[x+y] += flag
            d2[x+N-y-1] += flag

        for i, query in enumerate(queries):
            x, y = query

            if rows.get(x, 0) >= 1 or cols.get(y, 0) >= 1 or d1.get(x+y, 0) >= 1 or d2.get(x+N-y-1, 0) >= 1:
                res[i] = 1
                if grid.get(x, {}).get(y, None):
                    switch(x, y, -1)

                x1, y1 = x-1, y-1
                if 0 <= x1 < N and 0 <= y1 < N and grid.get(x1, {}).get(y1, None):
                    switch(x1, y1, -1)

                x2, y2 = x+1, y+1
                if 0 <= x2 < N and 0 <= y2 < N and grid.get(x2, {}).get(y2, None):
                    switch(x2, y2, -1)

                x3, y3 = x-1, y+1
                if 0 <= x3 < N and 0 <= y3 < N and grid.get(x3, {}).get(y3, None):
                    switch(x3, y3, -1)

                x4, y4 = x+1, y-1
                if 0 <= x4 < N and 0 <= y4 < N and grid.get(x4, {}).get(y4, None):
                    switch(x4, y4, -1)

                x5, y5 = x-1, y
                if 0 <= x5 < N and 0 <= y5 < N and grid.get(x5, {}).get(y5, None):
                    switch(x5, y5, -1)

                x6, y6 = x+1, y
                if 0 <= x6 < N and 0 <= y6 < N and grid.get(x6, {}).get(y6, None):
                    switch(x6, y6, -1)

                x7, y7 = x, y - 1
                if 0 <= x7 < N and 0 <= y7 < N and grid.get(x7, {}).get(y7, None):
                    switch(x7, y7, -1)

                x8, y8 = x, y + 1
                if 0 <= x8 < N and 0 <= y8 < N and grid.get(x8, {}).get(y8, None):
                    switch(x8, y8, -1)

        return res
