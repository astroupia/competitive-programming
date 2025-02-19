# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:       
        length = 0
        dummy_node = ListNode(-1, head)
        current_node = dummy_node
        while current_node:
            length += 1
            current_node = current_node.next

        tail = current_node
        n_index = length - n

        current_node = dummy_node
        for _ in range(n_index - 1):
            current_node = current_node.next
        
        if current_node.next == tail:
            current_node.next = None
        else:
            current_node.next = current_node.next.next
    
        return dummy_node.next
