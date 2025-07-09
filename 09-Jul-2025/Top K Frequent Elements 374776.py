# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map=Counter(nums)
        sorted_items=sorted(freq_map.items(),key=lambda x:x[1], reverse=True)
        res=[item[0] for item in sorted_items[:k]]
        return res
