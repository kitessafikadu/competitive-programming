# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def iterate(node, result):
            if not node:
                return False
            result += node.val            
            
            if not node.left and not node.right:
                return result == targetSum
            
            return (iterate(node.left, result) or
            iterate(node.right, result))
        result = 0
        return iterate(root, result)
