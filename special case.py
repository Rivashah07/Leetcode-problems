#problem 3120
class Solution(object):
    def numberOfSpecialChars(self, word):
        s=set(word)
        count=0
        for i in s:
            if i.isupper() and i.lower() in s:
                count+=1
        return count        
        