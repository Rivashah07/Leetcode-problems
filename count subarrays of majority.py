#3737 Count subarrays of majority Element 1
class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        arr = [1 if x == target else -1 for x in nums]

        prefix = 0
        prefixes = [0]

        for x in arr:
            prefix += x
            prefixes.append(prefix)

        sorted_vals = sorted(set(prefixes))
        rank = {v: i + 1 for i, v in enumerate(sorted_vals)}

        size = len(sorted_vals) + 2
        BIT = [0] * size

        def update(i):
            while i < size:
                BIT[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += BIT[i]
                i -= i & -i
            return s

        res = 0

        for p in prefixes:
            r = rank[p]
            res += query(r - 1)
            update(r)

        return res 