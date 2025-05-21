# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        n=int(''.join(map(str, b)))   
        return pow(a, n)%1337
