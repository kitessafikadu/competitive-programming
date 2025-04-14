# Problem: Largest Merge of Two Strings - https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res=[]
        i=j=0
        while i<len(word1) and j<len(word2):
            if word1[i:] > word2[j:]:
                res.append(word1[i])
                i+=1
            else:
                res.append(word2[j])
                j+=1
        return "".join(res)+word1[i:]+word2[j:]
        