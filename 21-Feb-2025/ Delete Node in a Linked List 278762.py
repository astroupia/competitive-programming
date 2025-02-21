# Problem:  Delete Node in a Linked List - https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        current_node = node 
        while current_node.next:
            current_node.val = current_node.next.val
            if current_node.next.next is None:
                current_node.next = None
                break 
            current_node = current_node.next
       
        