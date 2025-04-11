# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        s_count = Counter()
        res=[]

        for i in range(len(s)):
            s_count[s[i]] += 1
            if i >= len(p):
                left_char = s[i-len(p)]
                if s_count[left_char]==1:
                    s_count.pop(left_char)
                else:
                    s_count[left_char]-=1
            if s_count == p_count:
                res.append(i-len(p)+1)
        return res

