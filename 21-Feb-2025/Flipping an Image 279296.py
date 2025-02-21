# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            left, right = 0, len(row)-1
            while left <= right:
                row[left], row[right] = row[right] ^ 1, row[left] ^ 1
                left += 1
                right -= 1
        return image