#3536 Maximum Product of 2 Digits
class Solution(object):
    def maxProduct(self, n):
        m = sorted(str(n))
        return int(m[-1])*int(m[-2])