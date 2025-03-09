# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        is_negative = num < 0
        digits = list(str(abs(num)))

        if is_negative:
            digits.sort(reverse=True)
        else:
            digits.sort()

            if digits[0] == '0':
                for i in range(1, len(digits)):
                    if digits[i] != '0':
                        digits[0],digits[i] = digits[i],digits[0] 
                        break
        result = int(''.join(digits))
        return -result if is_negative else result
        