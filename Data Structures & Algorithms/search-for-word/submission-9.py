class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(x, y, i):
            if i == len(word):
                return True
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return False
            if (x, y) in visited or board[x][y] != word[i]:
                return False
            visited.add((x, y))
            found = (
                dfs(x + 1, y, i + 1) or
                dfs(x - 1, y, i + 1) or
                dfs(x, y + 1, i + 1) or
                dfs(x, y - 1, i + 1)
            )
            visited.remove((x, y))
            return found
            
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False