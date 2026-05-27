#31221
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}
        for i, ch in enumerate(word):
            if ch.islower():
                last_lower[ch] = i
            else:
                ch_low = ch.lower()
                if ch_low not in first_upper:
                    first_upper[ch_low] = i
        count = 0
        for ch in last_lower:
            if ch in first_upper and last_lower[ch] < first_upper[ch]:
                count += 1

        return count