# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummuy_node = ListNode(0)
        tail = dummuy_node
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            num1 = l1.val if l1 is not None else 0
            num2 = l2.val if l2 is not None else 0

            _sum = num1 + num2 + carry 
            digit = _sum % 10
            carry = _sum // 10

            new_node = ListNode(digit)
            tail.next = new_node
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return dummuy_node.next

