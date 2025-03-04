# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for x in range(len(arr), 1, -1):
            i = arr.index(x)
            if i:
                arr[: i+1] = arr[:i+1][::-1]
                res.append(i+1)
            arr[:x] = arr[:x][::-1]
            res.append(x)
        return res