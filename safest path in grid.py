#2812 Find the Safest Path in a Grid
import heapq
from collections import deque
class Solution(object):
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        INF = 10 ** 9

        #(DFS)
        dist = [[INF] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            x, y = q.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == INF:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        #(Max Heap)
        pq = [(-dist[0][0], 0, 0)]
        best = [[-1] * n for _ in range(n)]
        best[0][0] = dist[0][0]

        while pq:
            safe, x, y = heapq.heappop(pq)
            safe = -safe

            if x == n - 1 and y == n - 1:
                return safe

            if safe < best[x][y]:
                continue

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n:
                    newSafe = min(safe, dist[nx][ny])

                    if newSafe > best[nx][ny]:
                        best[nx][ny] = newSafe
                        heapq.heappush(pq, (-newSafe, nx, ny))

        return 0