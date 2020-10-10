"""
    834. 树中距离之和
    ----------------
"""
from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        dist_sums = [0 for _ in range(N)]
        node_nums = [1 for _ in range(N)]
        graph = {}

        for u, v in edges:
            graph.setdefault(u, [])
            graph.setdefault(v, [])
            graph[u].append(v)
            graph[v].append(u)

        def post_order(u, p):
            if u not in graph:
                node_nums[u] = 1
                return

            # dist_sums[u] = dis_sums[v] + node_nums[v]
            for v in graph[u]:
                if v == p:
                    continue

                post_order(v, u)

                node_nums[u] += node_nums[v]
                dist_sums[u] += dist_sums[v] + node_nums[v]

        def pre_order(u, p):
            if u not in graph:
                return

            for v in graph[u]:
                if v == p:
                    continue
                dist_sums[v] = dist_sums[u] + N - 2 * node_nums[v]
                pre_order(v, u)

        post_order(0, -1)
        pre_order(0, -1)

        return dist_sums
