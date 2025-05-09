# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)

        while left<=right:
            mid=(left+right)//2
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/mid)

            if hours<=h:
                right=mid-1
            else:
                left=mid+1
        return left
