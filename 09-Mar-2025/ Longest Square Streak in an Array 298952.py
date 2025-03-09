# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_streak = -1

        for num in nums:
            streak = 0
            while num in num_set:
                streak += 1
                num = num * num
            if streak > 1:
                max_streak = max(max_streak, streak)
        return max_streak

