# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0, len(height)-1
        max_water = float('-inf')

        while left < right:
            cur_water = min(height[left] , height[right]) * (right-left)
            max_water = max(max_water, cur_water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water