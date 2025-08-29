# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent={}
        def find(c):
            if c not in parent:
                parent[c]=c
            while c!=parent[c]:
                parent[c]=parent[parent[c]]
                c=parent[c]
            return c
        def union(c1, c2):
            p1,p2=find(c1),find(c2)
            if p1>p2:
                parent[p1]=p2
            else:
                parent[p2]=p1
        for c1,c2 in zip(s1, s2):
            union(c1,c2)
        res=''
        for c in baseStr:
            res+=find(c)
        return res