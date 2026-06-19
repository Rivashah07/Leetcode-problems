#1732 find highest altitude
class Solution(object):
    def largestAltitude(self, gain):
        curr = 0
        highest = 0
        for g in gain:
            curr += g
            highest = max(highest, curr)
        return highest