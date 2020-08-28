"""
    657. 机器人能否返回原点
    ---------------------
    比较四个方向移动的次数。相反方向出现的次数一定要相同。
    或者模拟移动，计算最后的坐标。
"""
from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counter = Counter(moves)
        for move in ('R', 'L', 'U', 'D'):
            if move not in counter:
                counter[move] = 0

        return counter['R'] == counter['L'] and counter['U'] == counter['D']
