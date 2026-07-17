#3312 Sorted GCD pairs Queries
from bisect import bisect_right
class Solution(object):
    def gcdValues(self, nums, queries):
        mx = max (nums)
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1
        cnt = [0] * (mx + 1)
        for g in range(1, mx + 1):
            for multiple in range(g, mx + 1, g):
                cnt[g] += freq[multiple]
        exact = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            c = cnt[g]
            pairs = c * (c - 1) // 2

            multiple = 2 * g
            while multiple <= mx:
                pairs -= exact[multiple]
                multiple += g

            exact[g] = pairs
            prefix = []
        values = []

        total = 0
        for g in range(1, mx + 1):
            if exact[g]:
                total += exact[g]
                prefix.append(total)
                values.append(g)

        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(values[idx])

        return ans