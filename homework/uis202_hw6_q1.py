from DoublyLinkedList import *
class LinkedQueue:
    def __init__(self):
        self.data=DoublyLinkedList()
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return (len(self)==0)
    def enqueue(self,item):
        self.data.add_last(item)
    def dequeue(self):
        return self.data.delete_first()
    def first(self):
        return self.data.header.next.data

        
    
