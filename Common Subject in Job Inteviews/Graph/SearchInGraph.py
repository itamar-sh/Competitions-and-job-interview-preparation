import math
from typing import List


class Solution:
    def _get_neighbors_from_edges_list_undirected_graph(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        neighbors = [[] for i in range(n)]
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)
        return neighbors

    def _get_neighbors_from_edges_list_directed_graph(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        neighbors = [[] for i in range(n)]
        for n1, n2 in edges:
            neighbors[n1].append(n2)
        return neighbors

    def validPathST(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbors = self._get_neighbors_from_edges_list_undirected_graph(n, edges)
        seen = set()
        queue = [source]
        while queue:
            vertex = queue.pop()
            if vertex == destination:
                return True
            for neighbor in neighbors[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return False

    # n = num of vertices, every vertex is an int. every edge is [int,int]
    # run time is O(V+E)
    def intBFS(self, n: int, edges: List[List[int]], s: int):
        neighbors = self._get_neighbors_from_edges_list_undirected_graph(n, edges)
        labels = [1]*n  # 0 is current, 1 is not_visited, 2 is visited
        labels[s] = 0  # s label is current
        dists = [math.inf]*n  # distance from s
        dists[s] = 0  # s dist from s is 0.
        pais = [None]*n  # prev vertex
        queue = [s]
        while queue:
            vertex = queue.pop()
            for neighbor in neighbors[vertex]:
                if labels[neighbor] == 1:  # not visited
                    labels[neighbor] = 0
                    pais[neighbor] = vertex
                    dists[neighbor] = dists[vertex] + 1
                    queue.append(neighbor)
            labels[vertex] = 2
        return dists

    # def _DFS_visit(self):
    #     labels[cur] = 0
    #     time += 1
    #     dists[cur] = time
    #     for neighbor in neighbors[cur]:
    #         if labels[neighbor] == 1:  # not visited
    #             pais[neighbor] = cur
    #             self._DFS_visit()
    #
    #         labels[neighbor] = 0
    #         dists[neighbor] = dists[vertex] + 1
    #         queue.append(neighbor)

    # n = num of vertices, every vertex is an int. every edge is [int,int]
    # run time is O(V+E)
    # def intDFS(self, n: int, edges: List[List[int]], s: int):
    #     labels = [1]*n
    #     time: int = 0
    #     dists = [math.inf]*n



    def tests(self):
        vertices1 = 3  # 4 vertices with name "0","1","2"
        graph1 = [[0,1],[0,2],[1,2]]
        assert([0,1,1] == (self.intBFS(vertices1, graph1, 0)))
        vertices2 = 4  # 4 vertices with name "0","1","2"
        graph2 = [[0, 1], [0, 2], [1, 2], [2,3]]
        assert([0,1,1,2] == (self.intBFS(vertices2, graph2, 0)))
        vertices3 = 4  # 4 vertices with name "0","1","2"
        graph3 = [[0, 1], [0, 2], [1, 2], [2, 3]]
        assert ([1, 1, 0, 1] == (self.intBFS(vertices3, graph3, 2)))



if __name__ == '__main__':
    solver = Solution()
    solver.tests()
