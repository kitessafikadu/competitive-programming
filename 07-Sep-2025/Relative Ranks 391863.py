# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        indexed_scores = [(s, i) for i, s in enumerate(score)]
        indexed_scores.sort(reverse=True, key=lambda x: x[0])
        result = [""] * n
        for rank, (s, i) in enumerate(indexed_scores, start=1):
            if rank == 1:
                result[i] = "Gold Medal"
            elif rank == 2:
                result[i] = "Silver Medal"
            elif rank == 3:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(rank)
        return result
