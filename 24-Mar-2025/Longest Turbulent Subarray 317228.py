# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        cur_len,longest = 0,0
        for i in range(len(arr)):
            if i >= 2 and (arr[i-2]>arr[i-1]<arr[i] 
            or arr[i-2] < arr[i-1] > arr[i]):
                cur_len+=1
            elif i >= 1 and arr[i-1] != arr[i]:
                cur_len=2
            else:
                cur_len=1
            longest = max(longest, cur_len)
        return longest
