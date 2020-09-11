"""
    210. 课程表 II
    --------------
    dfs + finish数组。dfs应该可以剪枝。
"""
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = {}
        degree = {i: 0 for i in range(numCourses)}
        for prerequisite in prerequisites:
            u, v = prerequisite
            g.setdefault(v, [])
            g[v].append(u)
            degree[u] += 1

        degree = sorted(degree.items(), key=lambda x: x[1])
        if degree[0][1] != 0:
            return []

        visited = [0] * numCourses
        finish = [0] * numCourses

        def dfs(u, h):
            finish[u] = max(finish[u], h)
            if u not in g:
                visited[u] = 2
                return True

            visited[u] = 1
            for v in g[u]:
                if visited[v] != 1:
                    flag = dfs(v, h + 1)
                    if not flag:
                        return False
                elif visited[v] == 1:
                    return False

            visited[u] = 2
            return True

        for u, _ in degree:
            if visited[u]:
                continue
            if not dfs(u, 0):
                return []

        res = {i: [] for i in range(numCourses)}

        for i, h in enumerate(finish):
            res[h].append(i)

        ans = []
        for value in res.values():
            ans += value

        return ans
