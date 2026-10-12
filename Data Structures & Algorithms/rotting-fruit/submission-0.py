class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    grid[r][c] = 1
                    queue.append([r,c,0])
        while queue:
            r,c,t = queue.popleft()
            if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]):
                continue
            if grid[r][c] == 0 or grid[r][c] == 2:
                continue
            grid[r][c] = 2
            queue.append([r + 1, c, t + 1])
            queue.append([r - 1, c, t + 1])
            queue.append([r, c + 1, t + 1])
            queue.append([r, c - 1, t + 1])
            m = max(t, m)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return m
        
            
