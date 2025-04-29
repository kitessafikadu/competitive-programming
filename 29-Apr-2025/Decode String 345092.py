# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()  # remove the '['
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(substr * int(k))
        return ''.join(stack)
