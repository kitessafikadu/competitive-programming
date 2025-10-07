# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class Solution:
    def partitionString(self, s: str) -> list[str]:
        result = []
        seen = set()
        current = ""

        for ch in s:
            current += ch
            if current not in seen:
                result.append(current)
                seen.add(current)
                current=""

        return result
