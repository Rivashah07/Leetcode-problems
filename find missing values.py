#3731 Find misssing values
class Solution:
    def findMissingValues(self, nums):
        seen = set(nums)
        lo, hi = min(nums), max(nums)
        return [x for x in range(lo, hi + 1) if x not in seen]