from ArrayStack import *
from ArrayDeque import *
class MidStack:
    def __init__(self):
        self.data_stack=ArrayStack()
        self.data_deque=ArrayDeque()
        self.counter=1
    def __len__(self):
        return len(self.data_stack)+len(self.data_deque)
    def is_empty(self):
        return len(self)==0
    def push(self,e):
        if len(self)==0:
           self.data_stack.push(e)
           self.counter+=1
        else:
            if self.counter%2==0:
                self.data_deque.enqueue_last(e)
                self.counter+=1
            else:
                self.data_stack.push(self.data_deque.dequeue_first())
                self.data_deque.enqueue_last(e)
                self.counter+=1
    def mid_push(self,e):
        if len(self)==0:
           self.data_stack.push(e)
           self.counter+=1
        else:
            if self.counter%2==0:
               self.data_deque.enqueue_first(e)
               self.counter+=1
            else:
               self.data_stack.push(e)
               self.counter+=1
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            if len(self.data_deque)==0:
                return self.data_stack.top()
            else:
                return self.data_deque.last()
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            if self.counter<=3:
                self.counter=-1
                if len(self.data_deque)==0:
                    return self.data_stack.pop()
                else:
                    return self.data_deque.dequeue_last()
            else:
                if self.counter%2!=0:
                    self.data_deque.enqueue_first(self.data_stack.pop())
                    self.counter-=1
                    return self.data_deque.dequeue_last()
                else:
                    self.counter-=1
                    return self.data_deque.dequeue_last()





