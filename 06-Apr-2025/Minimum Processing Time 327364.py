# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        min_time = 0
        task_idx = 0
        for time in processorTime:
            min_time = max(min_time, time+tasks[task_idx]) 
            task_idx += 4
        return min_time


        