class MyQueue:

    def __init__(self):
        self.queue = []
        self.size = 0
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.size +=1
        

    def pop(self) -> int:
        self.size-=1
        elem = self.queue[0]
        self.queue.remove(self.queue[0])
        return elem
        

    def peek(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        if self.size >= 1:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()