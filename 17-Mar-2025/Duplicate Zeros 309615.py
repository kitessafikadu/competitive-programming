# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        n = len(arr)
        
        while i < n:
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                arr.pop()  
                i += 1  
            i += 1