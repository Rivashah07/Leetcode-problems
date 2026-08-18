# 3471 Find largest almost missing integer
class Solution:
    def largestInteger(self, nums, k):
        freq = [0] * 51

        for i in range(len(nums) - k + 1):
            for num in set(nums[i:i+k]):
                freq[num] += 1

        for num in range(50, -1, -1):
            if freq[num] == 1:
                return num

        return -1