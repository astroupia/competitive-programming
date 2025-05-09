# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = deque()
        level.append(root)
        res = []

        while level:
            next_level = []
            for _ in range(len(level)):
                node = level.popleft()
                if node:
                    next_level.append(node.val)
                    level.append(node.left)
                    level.append(node.right)
            if level:
                res.append(next_level)

        return res
        


            