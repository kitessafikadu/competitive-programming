# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap):
            req_days=1
            total=0
            for w in weights:
                if total+w>cap:
                    req_days+=1
                    total=0
                total+=w
            return req_days<=days
        left,right=max(weights),sum(weights)
        while left<=right:
            mid=(left+right)//2
            if canShip(mid):
                right=mid-1
            else:
                left=mid+1
        return left