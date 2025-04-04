# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        start_with_index = sorted((start, i) for i, (start, end) in enumerate(intervals))
        starts = [s[0] for s in start_with_index]
        result = []
        for start, end in intervals:
            idx = bisect.bisect_left(starts, end)
            if idx < n:
                result.append(start_with_index[idx][1])
            else:
                result.append(-1)
        return result
