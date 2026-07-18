#1979 Find greatest common divisor of array
class Solution(object):
    def findGCD(self, nums):
        mn = min(nums)
        mx = max(nums)

        while mx:
            mn, mx = mx, mn % mx

        return mn