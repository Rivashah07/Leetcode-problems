#3718 Smallest missing multiple of K
class Solution(object):
    def missingMultiple(self, nums, k):
        s = set(nums)
        x = k

        while x in s:
            x += k

        return x