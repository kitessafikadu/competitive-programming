# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge1,edge2=edges[0],edges[1]

        return edge1[0] if edge1[0] in edge2 else edge1[1]