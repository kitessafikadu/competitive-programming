# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        for char in s:
            if char=='(':
                stack.append(0)
            else:
                last=stack.pop()
                if last==0:
                    stack[-1]+=1
                else:
                    stack[-1]+=2*last
        return stack[0]
