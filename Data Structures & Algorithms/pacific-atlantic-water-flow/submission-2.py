class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
         # (r, c) : [canFlowPacific?, canFlowAtlantic?]
        flow_mapping = {}
        numRows = len(heights)
        numCols = len(heights[0])
        DIRS = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(r, c, i, prev):
            if (r,c) in flow_mapping and flow_mapping[(r,c)][i]:
                return
            if r < 0 or r == numRows or c < 0 or c == numCols:
                return
            if prev and heights[r][c] < prev:
                return
            if (r,c) not in flow_mapping:
                flow_mapping[(r,c)] = [False, False]
            flow_mapping[(r,c)][i] = True

            for d in DIRS:
                dfs(r + d[0], c + d[1], i, heights[r][c])
            

        for i in range(numCols):
            dfs(0, i, 0, None)
        for i in range(numRows):
            dfs(i, 0, 0, None)


        for i in range(numCols):
            dfs(numRows - 1, i, 1, None)
        for i in range(numRows):
            dfs(i, numCols - 1, 1, None)

        res = []
        for r in range(numRows):
            for c in range(numCols):
                if (r,c) in flow_mapping and flow_mapping[(r,c)][0] and flow_mapping[(r,c)][1]:
                    res.append([r, c])
        return res

