from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(node):
            # go deep starting from one node in both directions
            left = self.dfs(node.left)
            right = self.dfs(node.right)

            # is our new diameter better than our running maximum
            self.max_diameter = max(self.max_diameter, left + right)
            return 1 + max(left,right) # returns our running diameter
        
        dfs(root)
        return self.max_diameter
