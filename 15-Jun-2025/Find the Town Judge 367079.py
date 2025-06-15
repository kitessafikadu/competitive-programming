# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta=defaultdict(int) #incoming-outgoing = n-1
        for src,dst in trust:
            delta[src]-=1
            delta[dst]+=1
        for i in range(1,n+1):
            if delta[i]==n-1:
                return i
        return -1