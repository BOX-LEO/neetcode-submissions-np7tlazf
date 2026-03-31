class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h = len(board)
        w = len(board[0])
        l = len(word)
        self.result = False

        def dfs(order,x=0,y=0,path:list=[]):
            if self.result:
                return
            if order==0:
                for i in range(h): #y
                    for j in range(w): #x
                        if board[i][j]==word[order]:
                            if order == l-1:
                                self.result = True
                                return
                            path.append([j,i])
                            dfs(order+1,j,i)
                            path.pop()
            else:
                neighbor = [[-1,0],[0,-1],[1,0],[0,1]]
                for n in neighbor:
                    nx, ny = x+n[0],y+n[1]
                    if  nx >=0 and nx<w and ny>=0 and ny<h and [nx,ny] not in path:
                        print(board[ny][nx],word[order])
                        if board[ny][nx]==word[order]:
                            if order == l-1:
                                self.result = True
                                return
                            path.append([nx,ny])
                            dfs(order+1,nx,ny)
                            path.pop()
        dfs(0)
        return self.result


            
            