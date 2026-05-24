class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        smaller_count = {}
        for i, num in enumerate(sorted_nums):
            if num not in smaller_count:
                smaller_count[num] = i

        ans = []

        for num in nums:
            ans.append(smaller_count[num])

        return ans
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        