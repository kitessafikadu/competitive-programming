# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        sorted_nums = sorted([int(x) for x in nums], reverse=True)
        return str(sorted_nums[k-1])