# 3689 maximum total subarray value 1

class Solution(object):
    def maxTotalValue(self, nums, k):
        mx = max(nums)
        mn = min(nums)

        return k * (mx - mn)