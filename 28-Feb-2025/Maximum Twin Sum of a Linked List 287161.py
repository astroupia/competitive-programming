# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        curr = head
        _MAX = float("-inf")

        while curr if curr is not None else None:
            stack.append(curr.val)
            curr = curr.next
        
        for i in range(len(stack)):
            index = len(stack) - 1 - i
            if 0 <= index <= (len(stack) / 2) - 1:
                _sum = stack[i] + stack[index]
                _MAX = max(_MAX, _sum)

        return _MAX
        
