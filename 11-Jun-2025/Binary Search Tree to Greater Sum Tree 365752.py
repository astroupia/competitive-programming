# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total_sum = 0

        def reverse_in_order(node):
            if not node:
                return

            # Visit right subtree
            reverse_in_order(node.right)
            
            # Process current node
            self.total_sum += node.val
            node.val = self.total_sum
            
            # Visit left subtree
            reverse_in_order(node.left)

        reverse_in_order(root)
        return root