class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        numRows = len(grid)
        numCols = len(grid[0])
        DIRS = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()

        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == 0:
                    queue.append((r,c,0))

        while queue:
            r, c, d = queue.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < numRows and 0 <= nc < numCols and grid[nr][nc] == 2147483647:
                    queue.append((nr, nc, d + 1))
                    grid[nr][nc] = d + 1
        