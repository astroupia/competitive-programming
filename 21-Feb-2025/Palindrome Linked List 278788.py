# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current_node = head
        stack = []

        while current_node:
            stack.append(current_node.val)
            current_node = current_node.next
        
        return stack == stack[::-1]
