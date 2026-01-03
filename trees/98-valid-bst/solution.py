from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # we need to do a dfs, each node will have a min and max
        def is_valid(node, minn, maxx):
            # base case: NULL -> True
            if not node:
                return True

            # if !(min < node < max) -> violates -> return False
            if node.val <= minn or node.val >= maxx:
                return False

            # -> left node -> update max
            # -> right node -> update min
            return (
                is_valid(node.left, minn, node.val) and
                is_valid(node.right, node.val, maxx)
            )

        # call on our root, with -inf and inf
        return is_valid(root, float("-inf"), float("inf"))