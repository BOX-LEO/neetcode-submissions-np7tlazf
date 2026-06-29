class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        neighbors = ((0,1),(0,-1),(1,0),(-1,0))
        length = len(word)
        rows, columns = len(board),len(board[0])
        self.res = False
        def dfs(row,col,index:int):
            if index == length:
                self.res = True
                return
            if not 0<=row<rows or not 0<=col<columns:
                return
            temp = board[row][col]
            if temp == word[index]:
                board[row][col] = '*'
                for dr, dc in neighbors:
                    dfs(row+dr,col+dc,index+1)
                board[row][col] = temp
        
        for r in range(rows):
            for c in range(columns):
                if self.res:
                    return self.res
                dfs(r,c,0)
        return self.res