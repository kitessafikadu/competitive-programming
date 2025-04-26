# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                stack_index = stack.pop()
                res[stack_index] = (i - stack_index)
            stack.append(i)
        return res
