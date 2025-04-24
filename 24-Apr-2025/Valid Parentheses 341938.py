# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}

        for bracket in s:
            if bracket in brackets:
                if stack and stack[-1] == brackets[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        return not stack
        