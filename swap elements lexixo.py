#2948 Make lexicographically  array by swapping elements
class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # (value, original index)
        arr = sorted((x, i) for i, x in enumerate(nums))

        ans = nums[:]
        l = 0

        while l < n:
            r = l

            # Find all values connected by valid swaps
            while r + 1 < n and arr[r + 1][0] - arr[r][0] <= limit:
                r += 1

            # Get values and their original indices
            values = [arr[i][0] for i in range(l, r + 1)]
            indices = sorted(arr[i][1] for i in range(l, r + 1))

            # Smallest values → smallest indices
            for i in range(len(values)):
                ans[indices[i]] = values[i]

            l = r + 1

        return ans