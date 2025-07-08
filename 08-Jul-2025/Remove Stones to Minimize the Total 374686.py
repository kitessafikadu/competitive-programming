# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i, pile in enumerate(piles):
            piles[i]=-pile
        heapq.heapify(piles)
        while k>0:
            num=heapq.heappop(piles)
            heapq.heappush(piles, (num+abs(num)//2))
            k-=1
        return -sum(piles)