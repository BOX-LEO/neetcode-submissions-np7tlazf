class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid),len(grid[0])
        neighbor = ((0,1),(0,-1),(1,0),(-1,0))
        dq = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==0:
                    dq.append((r,c))
        
        distance = 1
        while dq:
            for _ in range(len(dq)):
                x,y = dq.popleft()
                for dx,dy in neighbor:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]>distance:
                        grid[nx][ny] = distance #visited
                        dq.append((nx,ny))
            distance+=1



