# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
    
        for i in range(2 * n):
            num = nums[i % n]
            while stack and nums[stack[-1]] < num:
                m = stack.pop()
                res[m] = num
            if i < n:
                stack.append(i)
        return res