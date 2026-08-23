#1927 Sum Game
class Solution(object):
    def sumGame(self, num):
        n = len(num) // 2

        diff = 0
        q = 0

        for i in range(n):
            if num[i] == '?':
                q += 1
            else:
                diff += int(num[i])

        for i in range(n, 2 * n):
            if num[i] == '?':
                q -= 1
            else:
                diff -= int(num[i])

        return 2 * diff != -9 * q