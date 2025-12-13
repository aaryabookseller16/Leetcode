from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: #empty tree
            return []
        
        queue = deque()
        queue.append(root)
        ans = []

        while queue: # process every node O(N)
            level = [] # inner list
            n = len(queue) # n is the length of the upcoming level

            # process one level
            for i in range(n):
                node = queue.popleft()
                level.append(node.val)

                # add left sub child (if it exists) to our queue
                if node.left:
                    queue.append(node.left)

                # add right sub child (if it exists) to our queue
                if node.right:
                    queue.append(node.right)

            ans.append(level)


        # Time: O(n)
        # Space: O(n)

        return ans