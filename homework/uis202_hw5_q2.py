from ArrayStack import *
class MaxStack:
    def __init__(self):
        self.data=ArrayStack()
        self.highest_elem=None
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self)==0
    def push(self,e):
        if self.is_empty():
            self.data.push((e,e))
            self.highest_elem=e
        else:
            if e>self.highest_elem:
                self.highest_elem=e
                self.data.push((e,self.highest_elem))
            else:
                self.data.push((e,self.highest_elem))
    def top(self):
        if self.is_empty():
            raise Exception("stack is empty")
        else:
            return self.data.top()[0]
    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty")
        else:
            return self.data.pop()[0]
    def max(self):
        if self.is_empty():
            raise Exception("stack is empty")
        else:
            return self.data.top()[-1]

    
       
