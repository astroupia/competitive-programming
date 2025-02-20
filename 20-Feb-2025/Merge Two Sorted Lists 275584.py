# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left, right = 0, 0
        first_list, second_list = list1, list2
    
        dummy_node = ListNode()
        current_node = dummy_node

        while first_list or second_list:

            if not second_list or (first_list and first_list.val <= second_list.val):
                new_node = ListNode(first_list.val)
                current_node.next = new_node
                current_node = current_node.next
                first_list = first_list.next
                continue 
            
            new_node = ListNode(second_list.val)
            current_node.next = new_node 
            current_node = current_node.next
        
            
            second_list = second_list.next

        return dummy_node.next

