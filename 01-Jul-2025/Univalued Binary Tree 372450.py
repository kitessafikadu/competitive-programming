# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue=deque([root])
        target=root.val

        while queue:
            node=queue.popleft()
            if node.val != target:
                return False
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return True