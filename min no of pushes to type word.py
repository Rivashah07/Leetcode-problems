#3014 Minimum Number of Pushes to Type a Word 1
class Solution(object):
    def minimumPushes(self, word):
        return sum(i // 8 + 1 for i in range(len(word)))