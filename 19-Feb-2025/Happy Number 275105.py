# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # def get_next(num):
        #     total = 0
        #     while num > 0:
        #         digit = num % 10  # Get last digit
        #         total += digit * digit  # Square and add
        #         num //= 10  # Remove last digit
        #     return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))

        return n == 1

