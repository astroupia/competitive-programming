# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        self.tail = None
        self.length = 0
        self.dummuy_node = Node()

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        else:
            current_node = self.dummuy_node
            for _ in range(index + 1):
                current_node = current_node.next
            
            return current_node.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.dummuy_node.next
        self.dummuy_node.next = new_node
        self.length += 1

        if not self.tail:
            self.tail = new_node

    def addAtTail(self, val: int) -> None:

        new_node = ListNode(val)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        
        if not self.dummuy_node.next:
            self.addAtHead(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return 

        new_node = Node(val)
        if index == self.length:
            self.addAtTail(val)

        else:
            current_node = self.dummuy_node  
            for _ in range(index):
                current_node = current_node.next
            
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1
       

    def deleteAtIndex(self, index: int) -> None:    
        if index >= self.length:
            return 

        current_node = self.dummuy_node
        for _ in range(index ):
            current_node = current_node.next
        
        if current_node.next == self.tail:
            self.tail = current_node
        current_node.next = current_node.next.next
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)