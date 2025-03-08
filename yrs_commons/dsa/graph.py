# BFS for Graph/Tree - O(V + E)
import heapq
from collections import deque


class GraphAlgo:
    @staticmethod
    def bfs(graph, start, visited=None):
        # visited = visited or set()
        if visited is None:  # pragma: no cover
            visited = set()

        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    @staticmethod
    def dfs(graph, start, visited=None):  # DFS for Graph/Tree - O(V + E)
        if visited is None:  # pragma: no cover
            visited = set()
        visited.add(start)

        for neighbor in graph[start]:
            if neighbor not in visited:
                GraphAlgo.dfs(graph, neighbor, visited)

    @staticmethod
    def has_cycle(graph):  # Detect Cycle in Directed Graph using DFS - O(V + E)
        visited = set()
        rec_stack = set()

        def dfs_cycle(vertex):
            visited.add(vertex)
            rec_stack.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    if dfs_cycle(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True

            rec_stack.remove(vertex)
            return False

        for vertex in graph:
            if vertex not in visited:
                if dfs_cycle(vertex):
                    return True
        return False

    @staticmethod
    def dijkstra(graph, start):  # Dijkstra's Shortest Path - O((V + E) log V)
        distances = {vertex: float("infinity") for vertex in graph}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances


def topological_sort(number_of_nodes, edges):
    adjacency_list = {i: [] for i in range(number_of_nodes)}  ## Step 1: Create adjacency list and in-degree dictionary
    in_degree = {i: 0 for i in range(number_of_nodes)}

    for source, destination in edges:  ## Step 2: Build graph
        adjacency_list[source].append(destination)
        in_degree[destination] += 1

    zero_in_degree_queue = deque()  ## Step 3: Initialize queue with nodes having in-degree of 0
    for node in in_degree:
        if in_degree[node] == 0:
            zero_in_degree_queue.append(node)

    topological_order = []  ## Step 4: Perform topological sorting

    while zero_in_degree_queue:
        current_node = zero_in_degree_queue.popleft()
        topological_order.append(current_node)

        # Reduce in-degree of neighboring nodes
        for neighbor in adjacency_list[current_node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree_queue.append(neighbor)

    if len(topological_order) != number_of_nodes:  ## Step 5: Check for cycle in graph
        raise ValueError("The graph contains a cycle, topological sorting is not possible.")

    return topological_order
