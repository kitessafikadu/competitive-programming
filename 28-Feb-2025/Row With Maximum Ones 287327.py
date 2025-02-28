# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_count = 0
        min_index = 0
        for i in range(len(mat)):
            count = mat[i].count(1)
            if count > max_count:
                max_count = count
                min_index = i

        return [min_index, max_count]
