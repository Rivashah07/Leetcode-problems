#3345 Smallest Divisible Digit product 1
class Solution:
    def smallestNumber(self, n, t):
        while True:
            p=n
            pr=1
            while p>0:
                pr*=p%10
                p//=10
            if pr%t==0:
                return n
            n+=1