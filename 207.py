"""
    207. 课程表
    ----------
    拓扑排序。DFS方法基于这样的一个实施，对一个路径进行DFS遍历的时候，不能遍历到正在遍历的节点。
    BFS基于每个节点的入度。每次从入度为0的节点开始BFS遍历。遍历后的节点入度减一。
    只有当每个节点都被遍历后，才是正确结果。
"""
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]

        for edge in prerequisites:
            u, v = edge
            adjacency[u].append(v)

        def dfs(u):
            if visited[u] == 1:
                return False
            visited[u] = 1
            for v in adjacency[u]:
                if visited[v] == 1:
                    return False

                if visited[v] == 0 and not dfs(v):
                    return False

            visited[u] = 2
            return True

        for i in range(numCourses):
            if visited[i] == 0 and not dfs(i):
                return False

        return True
