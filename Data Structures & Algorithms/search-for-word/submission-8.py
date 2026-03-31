class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board),len(board[0])
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        def backtrack(coord,k):
            if k == len(word):
                return True
            r,c = coord
            if r<0 or r>=rows or c<0 or c>=cols:
                return False
            if board[r][c]==word[k]:
                temp = board[r][c]
                board[r][c] = '#'
                for dr,dc in direction:
                    res = backtrack((r+dr,c+dc),k+1)
                    if res:
                        return True
                board[r][c] = temp
            return False
        for i in range(rows):
            for j in range(cols):
                if backtrack((i,j),0):
                    return True
        return False
                
