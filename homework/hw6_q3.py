from DoublyLinkedList import *
class CompactString:
    def __init__(self, orig_str):
        self.data=DoublyLinkedList()
        for i in range(len(orig_str)):
            if i==0:
                self.data.add_last((orig_str[i],1))
            else:
                if orig_str[i]==orig_str[i-1]:
                    res=self.data.delete_last()[1]
                    res+=1
                    self.data.add_last((orig_str[i],res))
                else:
                    self.data.add_last((orig_str[i],1))
    def __add__(self,other):
        n3=CompactString("")
        curr=self.data.header.next
        self_len=sum([elem[1] for elem in self.data])
        other_len=sum([elem[1] for elem in other.data])
        res_self=curr.data[1]
        for i in range(self_len):
            if i==0:
                n3.data.add_last((curr.data[0],1))
                res_self-=1
            else:
                if res_self==0:
                    curr=curr.next
                    res_self=curr.data[1]
                if n3.data.trailer.prev.data[0]==curr.data[0]:
                    prev=n3.data.delete_last()
                    n3.data.add_last((curr.data[0],prev[1]+1))
                    res_self-=1
                else:
                    n3.data.add_last((curr.data[0],1))
                    res_self-=1
        curr_two=other.data.header.next
        res_other=curr_two.data[1]
        for i in range(other_len):
            if i==0:
                n3.data.add_last((curr_two.data[0],1))
                res_other-=1
            else:
                if res_other==0:
                    curr_two=curr_two.next
                    res_other=curr_two.data[1]
                if n3.data.trailer.prev.data[0]==curr_two.data[0]:
                    prev=n3.data.delete_last()
                    n3.data.add_last((curr_two.data[0],prev[1]+1))
                    res_other-=1
                else:
                    n3.data.add_last((curr_two.data[0],1))
                    res_other-=1
        return n3
    def __lt__(self,other):                               
        self_curr=self.data.header.next
        other_curr=other.data.header.next
        while (self_curr.data==other_curr.data) and self_curr is not None:
            self_curr=self_curr.next
            other_curr=other_curr.next
        if self_curr.data is None and other_curr.data is None:
            return False
        elif self_curr.data is not None and other_curr.data is None:
            return False
        elif self_curr.data is None and other_curr.data is not None:
            return True
        else:
            if ord(self_curr.data[0])==ord(other_curr.data[0]):
                if self_curr.data[1]>other_curr.data[1]:
                    if other_curr.next.data is None:
                        return False
                    else:
                        return ord(self_curr.data[0])<ord(other_curr.next.data[0])
                else:
                    if self_curr.next.data is None:
                        return True
                    else:
                        return ord(self_curr.next.data[0])<ord(other_curr.data[0])
            else:
                return ord(self_curr.data[0])<ord(other_curr.data[0])
    def __le__(self,other):
        self_curr=self.data.header.next
        other_curr=other.data.header.next
        while (self_curr.data==other_curr.data) and self_curr is not None:
            self_curr=self_curr.next
            other_curr=other_curr.next
        if self_curr.data is None and other_curr.data is None:
            return True
        elif self_curr.data is not None and other_curr.data is None:
            return False
        elif self_curr.data is None and other_curr.data is not None:
            return True
        else:
            if ord(self_curr.data[0])==ord(other_curr.data[0]):
                if self_curr.data[1]>other_curr.data[1]:
                    if other_curr.next.data is None:
                        return False
                    else:
                        return ord(self_curr.data[0])<ord(other_curr.next.data[0])
                else:
                    if self_curr.next.data is None:
                        return True
                    else:
                        return ord(self_curr.next.data[0])<ord(other_curr.data[0])
            else:
                return ord(self_curr.data[0])<ord(other_curr.data[0])           
    def __gt__(self,other):
        self_curr=self.data.header.next
        other_curr=other.data.header.next
        while (self_curr.data==other_curr.data) and self_curr is not None:
            self_curr=self_curr.next
            other_curr=other_curr.next
        if self_curr.data is None and other_curr.data is None:
            return False
        elif self_curr.data is not None and other_curr.data is None:
            return True
        elif self_curr.data is None and other_curr.data is not None:
            return False
        else:
            if ord(self_curr.data[0])==ord(other_curr.data[0]):
                if self_curr.data[1]>other_curr.data[1]:
                    if other_curr.next.data is None:
                        return True
                    else:
                        return ord(self_curr.data[0])>ord(other_curr.next.data[0])
                else:
                    if self_curr.next.data is None:
                        return False
                    else:
                        return ord(self_curr.next.data[0])>ord(other_curr.data[0])
            else:
                return ord(self_curr.data[0])>ord(other_curr.data[0])
    def __ge__(self,other):
        self_curr=self.data.header.next
        other_curr=other.data.header.next
        while (self_curr.data==other_curr.data) and self_curr is not None:
            self_curr=self_curr.next
            other_curr=other_curr.next
        if self_curr.data is None and other_curr.data is None:
            return True
        elif self_curr.data is not None and other_curr.data is None:
            return True
        elif self_curr.data is None and other_curr.data is not None:
            return False
        else:
            if ord(self_curr.data[0])==ord(other_curr.data[0]):
                if self_curr.data[1]>other_curr.data[1]:
                    if other_curr.next.data is None:
                        return True
                    else:
                        return ord(self_curr.data[0])>ord(other_curr.next.data[0])
                else:
                    if self_curr.next.data is None:
                        return False
                    else:
                        return ord(self_curr.next.data[0])>ord(other_curr.data[0])
            else:
                return ord(self_curr.data[0])>ord(other_curr.data[0])
    def __repr__(self):
        return "".join([(elem[0]*elem[1]) for elem in self.data])


