# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.s1 = []  # input stack
        self.s2 = []  # output stack
        
    def push(self, x: int) -> None:
        self.s1.append(x)
        
    def pop(self) -> int:
        self.peek()  # Ensure s2 has the front element
        return self.s2.pop()
        
    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
        
    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()