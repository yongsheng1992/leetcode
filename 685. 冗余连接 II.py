"""
    685. 冗余连接 II
    ---------------
    待优化
"""
from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        in_degree = {}
        out_degree = {}
        reversed_graph = {}
        graph = {}
        nodes = set()

        for edge in edges:
            u, v = edge
            nodes.add(u)
            nodes.add(v)
            in_degree.setdefault(v, 0)
            in_degree[v] += 1
            out_degree.setdefault(u, 0)
            out_degree[u] += 1
            reversed_graph.setdefault(v, [])
            graph.setdefault(u, [])
            reversed_graph[v].append(u)
            graph[u].append(v)

        stack = []

        def has_cycle(u):
            if u in stack:
                stack.append(u)
                return True

            stack.append(u)
            ans = False
            if u in graph:
                for v in graph[u]:
                    if has_cycle(v):
                        return True
            stack.pop(-1)

            return ans

        cyclic = False
        in_degree_list = sorted(in_degree.items(), key=lambda x: x[1])

        for u, _ in in_degree_list:
            if has_cycle(u):
                cyclic = True
                break

        if cyclic:
            print(stack)
            while stack[0] != stack[-1]:
                stack.pop(0)

            stack.pop(-1)
            if len(stack) == len(nodes):
                return edges[-1]

            edges_in_cycle = set()
            for i, _ in enumerate(stack[:-1]):
                if in_degree.get(stack[i+1], 0) == 2:
                    return [stack[i], stack[i+1]]
                edges_in_cycle.add((stack[i], stack[i+1]))

            if in_degree.get(stack[0], 0) == 2:
                return [stack[-1], stack[0]]
            edges_in_cycle.add((stack[-1], stack[0]))
            for u, v in reversed(edges):
                if (u, v) in edges_in_cycle:
                    graph[u].remove(v)
                    if has_cycle(v):
                        return [u, v]
                    graph[u].append(v)
            return [stack[-1], stack[0]]

        else:
            for u, degree in in_degree.items():
                if degree == 2:
                    return [reversed_graph[u][-1], u]

        return []
