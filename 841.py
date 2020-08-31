"""
    841. 钥匙和房间
    --------------
    将钥匙之间的关系转换为一个有向图，判断该图的连通性。这里使用dfs。
"""
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visit = set()

        def dfs(u):
            visit.add(u)
            for v in rooms[u]:
                if v not in visit:
                    dfs(v)

        dfs(0)
        return len(visit) == n
