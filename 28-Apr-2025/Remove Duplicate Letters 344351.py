# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        seen=set()
        counter=Counter(s)

        for c in s:
            counter[c]-=1
            if c in seen:
                continue
            while stack and c<stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)

        return ''.join(stack)
