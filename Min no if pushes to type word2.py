#3016 Minimum Number of Pushes to Type a Word 2
import collections
from collections import Counter
class Solution(object):
    def minimumPushes(self, word):
        return sum(
            f * (i // 8 + 1)
            for i, f in enumerate(
                sorted(Counter(word).values(), reverse=True)
            )
        )