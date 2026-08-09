#1140 Stone game II
class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            dp = [[0] * (n + 1) for _ in range(n + 1)]
            for i in range(n - 1, -1, -1):
                for m in range(1, n + 1):
                    for x in range(1, min(2 * m, n - i) + 1):
                        dp[i][m] = max(dp[i][m], suffix_sum[i] - dp[i + x][max(m, x)])
        return dp[0][1]