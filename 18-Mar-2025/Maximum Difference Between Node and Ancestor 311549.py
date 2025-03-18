# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_max(self, node, current_min, current_max):
        if not node:
            return current_max - current_min
        
        current_min = min(current_min, node.val)
        current_max = max(current_max, node.val)

        lt_diff = self.get_max(node.left, current_min, current_max)
        rt_diff = self.get_max(node.right, current_min, current_max) 
        return max(lt_diff, rt_diff) 
        
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        current_min, current_max = float("inf"), float("-inf")
        return self.get_max(root, current_min, current_max)  