# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(open=n, close=n, cur=""):
            if open==close==0:
                res.append(cur)
                return
            if open>0:
                backtrack(open-1,close, cur+"(")
            if open<close:
                backtrack(open, close-1, cur+")")
        backtrack()
        return res