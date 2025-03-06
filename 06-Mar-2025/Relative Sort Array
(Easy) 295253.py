# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0] * 1001

        for num in arr1:
            count[num] += 1
        
        res = []
        for num in arr2:
            res.extend([num]*count[num])
            count[num] = 0
        
        for num in range(1001):
            if count[num] > 0:
              res.extend([num]*count[num])

        return res
