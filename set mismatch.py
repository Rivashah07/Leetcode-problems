class Solution(object):
    def findErrorNums(self, nums):
        duplicate = 0

        for num in nums:
            if nums.count(num) == 2:
                duplicate = num
                break

        missing = 0

        for i in range(1, len(nums) + 1):
            if i not in nums:
                missing = i
                break

        return [duplicate, missing]
       

        

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        