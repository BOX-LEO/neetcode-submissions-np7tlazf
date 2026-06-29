class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid),len(grid[0])
        neighbor = ((0,1),(0,-1),(1,0),(-1,0))

        def bfs(r,c,distance):
            grid[r][c]=distance
            for dr,dc in neighbor:
                if 0<=r+dr<rows and 0<=c+dc<cols:
                    if grid[r+dr][c+dc]>distance+1:
                        bfs(r+dr,c+dc,distance+1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    bfs(r,c,0)

