class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        M = 10 ** 9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[i][j] = 1
        count = 0
        for i in range(1, N + 1):
            tmp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):

                    if i == m - 1:
                        count += dp[i][j]
                    if i == 0:
                        count += dp[i][j]
                    if j == n - 1:
                        count += dp[i][j]
                    if j == 0:
                        count += dp[i][j]

                tmp[i][j] = ((dp[i - 1][j] if i > 0 else 0) + (dp[i + 1][j] if i < (m - 1) else 0) + (
                    dp[i][j - 1] if j > 0 else 0) + (dp[i][j + 1] if j < (n - 1) else 0))

            print(dp)
            dp = tmp

        return count % M

s = Solution()
s.findPaths(2,2,2,0, 0)