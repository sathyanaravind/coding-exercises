class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r,c))
            area = 1

            while q:
                r, c = q.popleft()
                directions = [(-1,0), (1,0), (0,-1), (0,1)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(rows) and nc in range(cols) and (nr, nc) not in visited and grid[nr][nc] == 1):
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        area += 1
            return area 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    islandArea = bfs(r,c)
                    maxArea = max(islandArea, maxArea)
        
        return maxArea
        
