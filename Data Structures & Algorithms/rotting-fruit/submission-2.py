class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        DIRS = [(1,0),(-1,0),(0,-1),(0,1)]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append([r,c,0])
                if grid[r][c] == 1:
                    fresh += 1

        res = 0
        while queue and fresh > 0:
            r,c,t = queue.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    res = t + 1
                    queue.append([nr, nc, t + 1])
                    fresh -= 1

        if fresh > 0:
            return -1
        return res
        
            
