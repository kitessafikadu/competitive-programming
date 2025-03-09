# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        largest = len(arr)
        while largest > 0:
            idx = arr.index(largest)
            if idx != largest-1:
                if idx != 0:
                    arr[:idx+1] = arr[:idx+1][::-1]
                    res.append(idx+1)
                arr[:largest] = arr[:largest][::-1]
                res.append(largest)
            largest -= 1
        return res
                

