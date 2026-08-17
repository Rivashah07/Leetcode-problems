#1563 Stone game 5
class solution(object):
    def stoneGameV(self , a):
        n = len(a)
        dp = [[0] * n for _ in range(n)]
        mx = [[0] * n for _ in range(n)]

        for i in range(n):
            mx[i][i] = a[i]

        for r in range(1, n):
            mid = r
            left = a[r]
            right = 0

            for l in range(r - 1, -1, -1):
                left += a[l]

                while (right + a[mid]) * 2 <= left:
                    right += a[mid]
                    mid -= 1

                if right * 2 == left:
                    dp[l][r] = mx[l][mid]

                if mid != l:
                    dp[l][r] = max(dp[l][r], mx[l][mid - 1])

                if mid != r:
                    dp[l][r] = max(dp[l][r], mx[r][mid + 1])

                mx[l][r] = max(mx[l][r - 1], dp[l][r] + left)
                mx[r][l] = max(mx[r][l + 1], dp[l][r] + left)

        return dp[0][n - 1]