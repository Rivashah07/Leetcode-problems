#3116 Kth smallest amount with single denomination combination
class Solution(object):
    def findKthSmallest(self, coins, k):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            for mask in range(1, 1 << len(coins)):
                L = 1
                bits = 0

                for i in range(len(coins)):
                    if mask >> i & 1:
                        L = lcm(L, coins[i])
                        bits += 1

                        if L > x:
                            break

                if L <= x:
                    if bits % 2:
                        total += x // L
                    else:
                        total -= x // L

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left