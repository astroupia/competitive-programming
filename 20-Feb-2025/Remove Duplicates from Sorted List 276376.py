# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        prev_element = -1000
        current_node = head
        prev_node = head

        while current_node:
            if current_node.val == prev_element:
                prev_node.next = current_node.next
                current_node = current_node.next
            
            else:
                prev_node = current_node 
                prev_element = current_node.val
                current_node = current_node.next
        
        return head