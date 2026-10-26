from typing import List
from collections import deque

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        island_count = 0
        
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    total_value = 0
                    q = deque([(i, j)])
                    visited[i][j] = True
                    while q:
                        r, c = q.popleft()
                        total_value += grid[r][c]                       
                        for d in range(4):
                            nr, nc = r + dr[d], c + dc[d]
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append((nr, nc))                        
                    if total_value % k == 0:
                        island_count += 1
        return island_count