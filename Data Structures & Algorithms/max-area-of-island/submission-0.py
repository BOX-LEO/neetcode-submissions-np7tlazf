class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        neighbor = ((0,1),(0,-1),(1,0),(-1,0))
        self.res = 0
        def bfs(x,y):
            area = 0
            dq = deque()
            dq.append((x,y))
            grid[x][y]=0
            while dq:
                r,c = dq.popleft()
                area+=1
                for dr,dc  in neighbor:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        dq.append((nr,nc))
                        grid[nr][nc]=0
            if area>self.res:
                self.res = area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    bfs(row,col)
        return self.res