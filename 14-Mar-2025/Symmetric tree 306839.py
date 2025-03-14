# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_sys(left ,right):
            if None in [left, right]:
                return left is None and right is None

            res = left.val == right.val
            res = res and is_sys(left.right, right.left)
            res = res and is_sys(left.left, right.right)

            return res
        
        if is_sys(root.left, root.right):
            return True
        else:
            return False
