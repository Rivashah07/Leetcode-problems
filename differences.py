#2574 left and right sum differences
class Solution(object):
    def leftRightDifference(self, nums):
        totalSum = sum(nums)
        leftSum = 0
        answer = []

        for num in nums:
            rightSum = totalSum - leftSum - num
            answer.append(abs(leftSum - rightSum))
            leftSum += num

        return answer