#3838 mapping words to weights

class Solution:
    def generateTag(self, words, weights):
        for word in words:
            curr = 0
            for ch in word:
                curr += weights[ord(ch) - ord("a")]
            res += chr((25 - curr%26) + ord("a"))
        return res


