class LinkedStack:
    def __init__(self):
        self.data=DoublyLinkedList()
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self)==0
    def push(self,e):
        self.data.add_last(e)
    def top(self):
        if self.is_empty():
            raise Exception("stack is empty")
        return self.data.trailer.prev
    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty")
        return self.data.delete_last()
 def __getitem__(self,i):
        if i>len(self)-1:
            raise IndexError
        if float(i)>=len(self)/2:
            start_node=self.trailer
            pos=len(self)-1
            cursor=start_node.prev
            if len(self)%2==0:
                iterate=int(len(self)/2)
            else:
                iterate=int((len(self)-1)/2)
            for e in range(iterate):
                if pos==i:
                    return cursor.data
                else:
                    cursor=cursor.prev
                    pos=-1
        else:
            start_node=self.header
            pos=0
            cursor=start_node.next
            if len(self)%2==0:
                iterate=int(len(self)/2)
            else:
                iterate=int((len(self)+1)/2)
            for e in range(iterate):
                if pos==i:
                    return cursor.data
                else:
                    cursor=cursor.next
                    pos+=1
class MidStack:
    def __init__(self):
        self.data=DoublyLinkedList()
        self.middle=None
        self.runs=-1
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self)==0
    def push(self,e):
        if self.is_empty():
            self.data.add_last(e)
            self.runs+=1
            self.middle=self.data.header.next
        else:
            if self.runs%2==0:
                self.data.add_last(e)
                self.runs+=1
            else:
                self.data.add_last(e)
                self.runs+=1
                self.middle=self.middle.next
    def top(self):
        if self.is_empty():
            raise Exception("stack is empty")
        return self.data.trailer.prev
    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty")
        else:
            if self.runs%2!=0:
                self.middle=self.middle.prev
                self.runs-=1
                return self.data.delete_last()
            else:
                self.runs-=1
                return self.data.delete_last()
    def mid_push(self,e):
        if self.is_empty():
            raise Exception("stack is empty")
        else:
            self.data.add_after(self.middle,e)
class SinglyLinkedList:
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def disconnect(self):
        self.data = None
        self.next = None
    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0
    def __len__(self):
        return self.size
    def is_empty(self):
        return (len(self) == 0)
    def add_after(self,node,val):
        new_node=SinglyLinkedList.Node(val)
        new_node.next=node.next
        node.next=new_node
        if node==self.tail:
            self.tail=new_node
        self.size+=1
        return new_node
    def add_first(self,val):
        if self.is_empty():
            self.header=SinglyLinkedList.Node(val)
            self.tail=self.header
        else:
            new_node=SinglyLinkedList.Node(val)
            new_node.next=self.header
            self.header=new_node
        self.size+=1
        return self.header
    def add_last(self,val):
        self.last=self.add_after(self.tail,val)
        return self.last
    def delete_first(self):
        if self.is_empty():
            raise Exception("stack is empty")
        elif self.header==self.tail:
            val=self.header.data
            self.header.disconnect()
            self.header,self.tail=None,None
        else:
            deleted_node=self.header
            self.header=self.header.next
            val=deleted_node.data
            deleted_node.disconnect()
        self.size-=1
        return val
    def delete_last(self):
          if self.is_empty():
            raise Exception("stack is empty")
        elif self.header==self.tail:
            val=self.header.data
            self.header.disconnect()
            self.header,self.tail=None,None
        else:
            val=self.tail.data
            curr=self.header
            while curr.next is not self.tail:
                curr=curr.next
            curr.next=None
            self.tail.disconnect()
            self.tail=curr
        self.size-=1
        return val
    def reverse(self):
        prev=None
        curr,next=self.header,self.header
        while next:
            curr=next
            next=curr.next
            current.next,prev=prev,curr
        self.tail=self.header
        self.header=curr
    def __iter__(self):
        cursor = self.header.next
        while(cursor is not None):
            yield cursor.data
            cursor = cursor.next
    def __repr__(self):
        return "[" + " -> ".join([str(elem) for elem in self])+ "]
        

