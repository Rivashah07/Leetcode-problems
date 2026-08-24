#1872 Stone game VIII
class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)
        for i in range(1, n):
            stones[i] += stones[i - 1]
        dp = [0] * n
        dp[n - 1] = stones[n - 1]
        for i in range(n - 2, 0, -1):
            dp[i] = max(dp[i + 1], stones[i] - dp[i + 1])
        return dp[1]