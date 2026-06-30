class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        cells = []
        for r in range(rows):
            for c in range(cols):
                cells.append((matrix[r][c], r, c))

        cells.sort(reverse=True)

        dp = [[1] * cols for _ in range(rows)]
        ans = 1

        for val, r, c in cells:
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if matrix[nr][nc] > val:
                        dp[r][c] = max(dp[r][c], 1 + dp[nr][nc])

            ans = max(ans, dp[r][c])

        return ans