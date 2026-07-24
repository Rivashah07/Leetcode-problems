#3514 No of unique XOR triplets 2
class Solution(object):
    def uniqueXorTriplets(self, nums):
        vals = list(set(nums))
        n = len(vals)

        pair = set()

        for i in range(n):
            a = vals[i]
            for j in range(i, n):
                pair.add(a ^ vals[j])

        ans = set()

        for p in pair:
            for a in vals:
                ans.add(p ^ a)

        return len(ans)