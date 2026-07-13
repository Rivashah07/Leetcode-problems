#1291 Sequential Digits
class Solution(object):
    def sequentialDigits(self, low, high):
        s = "123456789"
        ans = []

        min_len = len(str(low))
        max_len = len(str(high))

        for length in range(min_len, max_len + 1):
            for start in range(10 - length):
                num = int(s[start:start + length])
                if low <= num <= high:
                    ans.append(num)

        return ans
    