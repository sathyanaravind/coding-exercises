class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        visited = set()
        rows = len(image)
        cols = len(image[0])
        res = image

        def bfs(sr, sc, color):
            q = deque()
            q.append((sr,sc))
            visited.add((sr,sc))
            temp = res[sr][sc]

            while  q:
                row, col = q.popleft()
                #if res[row][col] != color:
                res[row][col] = color
                
                directions = [(-1,0),(1,0),(0,-1),(0,1)]

                for dr, dc in directions:
                    r, c = row+dr, col+ dc

                    if  0 <= r < rows and 0 <= c < cols and res[r][c] == temp and (r,c) not in visited:
                        res[r][c] = color
                        visited.add((r,c))
                        q.append((r,c))
        
        bfs(sr, sc, color)
        return res



        
