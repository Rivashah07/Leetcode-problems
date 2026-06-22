#1189 maximum number of balloons
from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        c = Counter(text)

        return min(
            c['b'],
            c['a'],
            c['l'] // 2,
            c['o'] // 2,
            c['n']
        )