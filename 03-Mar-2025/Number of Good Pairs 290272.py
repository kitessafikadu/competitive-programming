# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

  def numIdenticalPairs(self, nums):
        count = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count