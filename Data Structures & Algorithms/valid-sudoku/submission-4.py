class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)
        for r in range(9):
            for c in range(9):
                n = board[r][c]
                if n =='.':
                    continue
                elif n in rows[r] or n in cols[c] or n in blocks[(r//3,c//3)]:
                    return False
                else:
                    rows[r].add(n)
                    cols[c].add(n)
                    blocks[(r//3,c//3)].add(n)
        return True