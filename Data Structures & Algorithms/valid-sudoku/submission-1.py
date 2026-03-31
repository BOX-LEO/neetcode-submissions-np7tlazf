class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(board: List[List[str]],r:int,c:int)->bool:
            target = board[r][c]
            if target=='.':
                return True
            count = 0
            for i in board[r]:
                if i==target:
                    count+=1
            for i in range(9):
                if board[i][c]==target:
                    count+=1
            rb=r//3
            cb=c//3
            for i in range(3):
                for j in range(3):
                    if board[rb*3+i][cb*3+j]==target:
                        count+=1
            return count==3

        for r in range(9):
            for c in range(9):
                if isValid(board,r,c):
                    continue
                else:return False
        return True
                





            