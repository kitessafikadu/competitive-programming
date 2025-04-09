# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1]*n
        window_size=2*k+1
        if window_size > n:
            return res
        window_sum=sum(nums[:window_size])
        res[k]=window_sum//window_size
        left = 0

        for right in range(window_size,n):
            window_sum+=nums[right]-nums[left]
            left+=1
            res[left+k]=window_sum//window_size
        return res