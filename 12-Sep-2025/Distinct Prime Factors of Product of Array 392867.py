# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes = set()
        def factorize(x):
            d = 2
            while d * d <= x:
                while x % d == 0:
                    primes.add(d)
                    x //= d
                d += 1
            if x > 1:
                primes.add(x)
        for num in nums:
            factorize(num)
        return len(primes)