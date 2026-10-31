class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # right[i][j]: paths arriving from the left
        # down[i][j]: paths arriving from above
        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        right[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    ways = 1
                else:
                    ways = (right[i][j] + down[i][j]) % MOD

                if ways == 0:
                    continue

                if grid[i][j] == 0:
                    # Move right
                    if j + 1 < n:
                        right[i][j + 1] = (
                            right[i][j + 1] + ways
                        ) % MOD

                    # Move down
                    if i + 1 < m:
                        down[i + 1][j] = (
                            down[i + 1][j] + ways
                        ) % MOD

                else:
                    # Mirror: arriving from the left
                    # reflects the robot downward
                    if i + 1 < m:
                        down[i + 1][j] = (
                            down[i + 1][j] + right[i][j]
                        ) % MOD

                    # Mirror: arriving from above
                    # reflects the robot to the right
                    if j + 1 < n:
                        right[i][j + 1] = (
                            right[i][j + 1] + down[i][j]
                        ) % MOD

        return (right[m - 1][n - 1] +
                down[m - 1][n - 1]) % MOD