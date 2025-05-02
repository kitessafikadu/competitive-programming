# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        folders=path.split("/")
        stack=[]
        for folder in folders:
            if folder == "" or folder==".":
                continue
            elif folder =="..":
                if stack: stack.pop()
            else:
                stack.append(folder)
        return "/" + "/".join(stack)


