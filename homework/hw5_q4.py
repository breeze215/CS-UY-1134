from ArrayStack import *
class Queue:
    def __init__(self):
        self.datastack_one=ArrayStack()
        self.datastack_two=ArrayStack()
    def __len__(self):
        return len(self.datastack_one)+len(self.datastack_two)
    def is_empty(self):
        return len(self)==0
    def enqueue(self,elem):
        self.datastack_one.push(elem)
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            for i in range(len(self.datastack_one)-1):
                self.datastack_two.push(self.datastack_one.pop())
            value=self.datastack_one.pop()
            for i in range(len(self.datastack_two)):
                self.datastack_one.push(self.datastack_two.pop())
            return value
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            for i in range(len(self.datastack_one)-1):
                self.datastack_two.push(self.datastack_one.pop())
            value=self.datastack_one.top()
            for i in range(len(self.datastack_two)):
                self.datastack_one.push(self.datastack_two.pop())
            return value

