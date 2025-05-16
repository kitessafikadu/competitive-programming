# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        def canMakeBouquets(day):
            bouquets = 0  
            flowers = 0   

            for bloom in bloomDay:
                if bloom <= day:  
                    flowers += 1
                    if flowers == k:  
                        bouquets += 1
                        flowers = 0   
                else:
                    flowers = 0  # broken sequence

            return bouquets >= m

        # 3. Binary Search over possible days
        left = min(bloomDay)
        right = max(bloomDay)
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                result = mid         
                right = mid - 1
            else:
                left = mid + 1       

        return result
