"""
    1030. 距离顺序排列矩阵单元格
    --------------------------
    使用广度优先搜索
"""
from typing import List
from collections import deque

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        flag = [[0 for _ in range(C)] for _ in range(R)]

        queue = deque()
        queue.append((r0, c0))
        res = []

        while queue:
            r, c = queue.popleft()
            if flag[r][c] == 1:
                continue

            flag[r][c] = 1
            res.append([r, c])

            for x, y in directions:
                r1 = r + x
                c1 = c + y

                if 0 <= r1 < R and 0 <= c1 < C:
                    queue.append([r1, c1])

        return res
