# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            n,x = -n,1/x
        smaller=self.myPow(x,n//2)
        return smaller*smaller*x if n%2 else smaller*smaller