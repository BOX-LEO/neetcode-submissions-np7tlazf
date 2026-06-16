class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                n = board[r][c]
                if n =='.':
                    continue
                elif n in rows[r] or n in cols[c] or n in blocks[r//3*3+c//3]:
                    return False
                else:
                    rows[r].add(n)
                    cols[c].add(n)
                    blocks[r//3+c//3].add(n)
        return True