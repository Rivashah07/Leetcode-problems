#3702 Longest Subsequence With Non-Zero bitwise XOR
class Solution(object):
    def longestSubsequence(self, nums):
        x = 0

        for num in nums:
            x ^= num

        if x:
            return len(nums)

        return len(nums) - 1 if any(nums) else 0