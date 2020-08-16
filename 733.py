"""
    733. 图像渲染
    ------------
    简单的图的dfs或者bfs。下面的代码flag可以不需要，使用队列代替。
"""
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        if m == 0:
            return image

        n = len(image[0])
        flag = [[False for _ in range(n)] for _ in range(n)]

        self.bfs(image, sr, sc, m, n, image[sr][sc], newColor, flag)
        return image

    def bfs(self, image, x, y, m, n, color, newColor, flag):
        if x < 0 or x >= m or y < 0 or y > n:
            return

        if image[x][y] != color:
            return

        if flag[x][y]:
            return

        flag[x][y] = True
        image[x][y] = newColor

        x0, y0 = x - 1, y
        x1, y1 = x + 1, y
        x2, y2 = x, y - 1
        x3, y3 = x, y + 1

        self.bfs(image, x0, y0, m, n, color, newColor, flag)
        self.bfs(image, x1, y1, m, n, color, newColor, flag)
        self.bfs(image, x2, y2, m, n, color, newColor, flag)
        self.bfs(image, x3, y3, m, n, color, newColor, flag)
