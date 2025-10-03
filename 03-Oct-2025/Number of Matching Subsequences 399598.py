# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = defaultdict(list)
        for word in words:
            it = iter(word)
            buckets[next(it)].append(it)
        
        count = 0
        for ch in s:
            current = buckets[ch]
            buckets[ch] = []
            for it in current:
                nxt = next(it, None)
                if nxt:
                    buckets[nxt].append(it)
                else:
                    count += 1
        
        return count
