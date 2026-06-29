#1967 Number of Strings that appear as Substrings in Word
class Solution(object):
    def numOfStrings(self, patterns, word):
        return sum(pattern in word for pattern in patterns)