class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows,cols = len(grid),len(grid[0])
        neighbor = [[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(r,c):
            grid[r][c]='0'
            for dr,dc in neighbor:
                if 0<=r+dr<rows and 0<=c+dc<cols and grid[r+dr][c+dc]=='1':
                    dfs(r+dr,c+dc)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] =='1':
                    # print(i,j)
                    res+=1
                    dfs(i,j)
        return res