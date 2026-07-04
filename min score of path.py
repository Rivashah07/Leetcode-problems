#2492 Minimum Score of a Path Between Two Cities
from collections import defaultdict, deque
class Solution:
    def minScore(self, n, roads):
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = set()
        min_score = float('inf')
        queue = deque([1])
        visited.add(1)

        while queue:
            node = queue.popleft()
            for neighbor, weight in graph[node]:
                min_score = min(min_score, weight)
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return min_score