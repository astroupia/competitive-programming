# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head

        dummy_node = ListNode(-1, head)
        current_node = dummy_node
        prev = current_node

        while current_node:
            if current_node.val == val:
                prev.next = current_node.next
            else:
                prev = current_node

            current_node = current_node.next
        
        return dummy_node.next