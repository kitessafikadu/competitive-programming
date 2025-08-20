# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        if num==0:
            return 1
        mask=(1<<num.bit_length())-1
        return num^mask