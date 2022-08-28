from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbors = [[] for i in range(n)]
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)
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