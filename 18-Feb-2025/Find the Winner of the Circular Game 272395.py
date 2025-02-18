# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        friends = list(range(1, n + 1))
        index = 0

        while len(friends) > 1:
            index = (index + k - 1) % len(friends)
            friends.pop(index)
        return friends[0]


        