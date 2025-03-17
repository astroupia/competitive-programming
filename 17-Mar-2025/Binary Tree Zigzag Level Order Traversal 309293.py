# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level = [root]
        nums = [[root.val]]
        depth = 0
        while level:
            level_nums = []
            next_level = []
            for node in level:
                if node.right:
                    next_level.append(node.right)
                    level_nums.append(node.right.val)

                if node.left:
                    next_level.append(node.left)
                    level_nums.append(node.left.val)

            level = next_level
            if level_nums:
                if depth % 2 == 0:
                    nums.append(level_nums)
                else:
                    nums.append(level_nums[::-1])
            depth += 1
        return nums