# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negatives = [num for num in nums if num < 0]
        positives = [num for num in nums if num > 0]

        ans = []
        for i in range(len(nums)//2):
            ans.append(positives[i])
            ans.append(negatives[i])        
        
        return ans