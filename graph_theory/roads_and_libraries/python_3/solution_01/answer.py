#!/bin/python3

import sys


class Solver:

    @staticmethod
    def dfs(graph, start):
        visited, stack = set(), set([start])
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.update(graph[vertex] - visited)
        return visited

    @staticmethod
    def get_query_cost(n, c_lib, c_road, graph):
        # break graph into components
        summary = 0
        undistributed_vertices = set(range(1, n + 1))
        while len(undistributed_vertices) > 0:
            component = Solver.dfs(graph, undistributed_vertices.pop())
            summary += c_lib * len(component) if c_lib <= c_road else c_lib + (len(component) - 1) * c_road
            undistributed_vertices -= component
        return summary


q = int(input().strip())
for query_idx in range(q):
    number_strings = input().strip().split(' ')
    n, m, c_lib, c_road = number_strings[0], number_strings[1], number_strings[2], number_strings[3]
    n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]

    graph = {city_idx: set() for city_idx in range(1, n + 1)}
    for road_idx in range(m):
        road_start, road_end = input().strip().split(' ')
        road_start, road_end = [int(road_start), int(road_end)]
        if road_start != road_end:
            graph[road_start].add(road_end)
            graph[road_end].add(road_start)
    print(Solver.get_query_cost(n, c_lib, c_road, graph))
