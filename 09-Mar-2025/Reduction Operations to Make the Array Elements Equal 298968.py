# Problem: Reduction Operations to Make the Array Elements Equal - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        steps = 0
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                steps += 1
            count += steps
        return count
