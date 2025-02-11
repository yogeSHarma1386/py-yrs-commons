
# BFS for Graph/Tree - O(V + E)
from collections import deque
import heapq


class Graph:
    @staticmethod
    def bfs(graph, start, visited=None):
        visited = visited or set()

        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            # Process vertex here

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    # DFS for Graph/Tree - O(V + E)
    @staticmethod
    def dfs(graph, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        # Process vertex here

        for neighbor in graph[start]:
            if neighbor not in visited:
                Graph.dfs(graph, neighbor, visited)

    # Detect Cycle in Directed Graph using DFS - O(V + E)
    @staticmethod
    def has_cycle(graph):
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

    # Dijkstra's Shortest Path - O((V + E) log V)
    @staticmethod
    def dijkstra(graph, start):
        distances = {vertex: float('infinity') for vertex in graph}
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
