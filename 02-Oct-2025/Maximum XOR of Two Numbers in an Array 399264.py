# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = {}
        for num in nums:
            node = root
            for k in range(31, -1, -1):
                bit = (num >> k) & 1
                if bit not in node:
                    node[bit] = {}
                node = node[bit]

        # Find maximum XOR
        ans = 0
        for num in nums:
            node = root
            cur = 0
            for k in range(31, -1, -1):
                bit = (num >> k) & 1
                opposite = 1 - bit
                if opposite in node:
                    cur |= (1 << k)
                    node = node[opposite]
                else:
                    node = node[bit]
            ans = max(ans, cur)

        return ans