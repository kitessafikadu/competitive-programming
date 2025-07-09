# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_map=Counter(words)
        sorted_words=sorted(freq_map.items(), key=lambda x:(-x[1],x[0]))
        return [word for word,freq in sorted_words[:k]]