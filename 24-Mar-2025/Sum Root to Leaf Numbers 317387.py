# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, currentNum) :
            if node is None: return 0
            currentNum = currentNum * 10 + node.val
            if node.left is None and node.right is None: return currentNum
            return self.dfs(node.left, currentNum) + self.dfs(node.right, currentNum)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)