class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        rows = len(board)
        cols = len(board[0])
        output = False
        def backtrack(cand,coord,visited):
            print(visited)
            nonlocal output
            if cand == word:
                output = True
            if len(cand)<len(word):
                for d in direction:
                    x = coord[0]+d[0]
                    y = coord[1]+d[1]
                    if 0<=x<rows and 0<=y<cols and [x,y] not in visited and board[x][y]==word[len(cand)]:
                        cand = cand+board[x][y]
                        visited.append([x,y])
                        backtrack(cand,[x,y],visited)
                        cand = cand[:-1]
                        visited.pop()

        for i in range(rows):
            for j in range(cols):
                print(i,j)
                if board[i][j] == word[0]:
                    visited = [[i,j]]
                    backtrack(word[0],(i,j),visited)
                    if output:
                        return True
        
        return False
            
            