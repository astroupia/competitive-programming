# Problem: Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums = []

        def traverse_post(node):
            if not node:
                return 
        
            traverse_post(node.left)
            traverse_post(node.right)
            nums.append(node.val)

        traverse_post(root)
        return nums
        