# 1840 Maximum building height
class Solution(object):
    def maxBuilding(self, n, restrictions):
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        restrictions.sort()
        m = len(restrictions)
        for i in range(1, m):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] +
                restrictions[i][0] -
                restrictions[i - 1][0]
            )
        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] +
                restrictions[i + 1][0] -
                restrictions[i][0]
            )
        ans = 0
        for i in range(1, m):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]

            d = x2 - x1

            peak = max(h1, h2) + (d - abs(h1 - h2)) // 2

            ans = max(ans, peak)

        return ans