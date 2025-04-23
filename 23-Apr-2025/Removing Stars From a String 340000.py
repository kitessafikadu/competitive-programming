# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution(object):
    def removeStars(self, s):
        stack = []

        for x in s:
            if x=="*" and stack:
                stack.pop()
            else:
                stack.append(x)

        return "".join(stack)