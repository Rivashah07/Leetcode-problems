#3090 Maaximum length substring with 2 occurence
class Solution(object):
    def maximumLengthSubstring(self, s):
        count = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            c = s[right]
            count[c] = count.get(c, 0) + 1

            while count[c] > 2:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans