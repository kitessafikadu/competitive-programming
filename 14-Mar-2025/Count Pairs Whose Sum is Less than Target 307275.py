# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        left, right = 0, len(nums)-1
        nums.sort()
        while left < right:
            if nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i >= j:
        #             continue
        #         elif nums[i] + nums[j] < target:
        #             count += 1
        return count

        