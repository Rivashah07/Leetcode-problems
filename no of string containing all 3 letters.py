#1358 Number of Substrings Containing All Three Characters 
class Solution(object):
    def numberOfSubstrings(self, s):
        last = {'a': -1, 'b': -1, 'c': -1}
        ans = 0

        for i, ch in enumerate(s):
            last[ch] = i
            ans += min(last.values()) + 1

        return ans