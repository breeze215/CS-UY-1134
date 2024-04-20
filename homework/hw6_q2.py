from DoublyLinkedList import *
class Integer:
    def __init__(self, num_str):
        self.data=DoublyLinkedList()
        for i in range(len(num_str)):
            self.data.add_last(num_str[i])
    def __add__(self,other):
        new_obj=DoublyLinkedList()
        curr1=self.data.trailer.prev
        curr2=other.data.trailer.prev
        carry=None
        for i in range(min(len(self.data),len(other.data))):
            res=0
            if carry is not None:
                res=int(curr1.data)+int(curr2.data)+int(carry)
            else:
                res=int(curr1.data)+int(curr2.data)
            res=str(res)
            if len(res)>1:
                carry=res[0]
                res=res[1]
            else:
                carry=None
            new_obj.add_first(res)
            curr1=curr1.prev
            curr2=curr2.prev
        if len(self.data)>len(other.data):
            pointer=curr1
        else:
            pointer=curr2
        for i in range(min(len(self.data),len(other.data)),max(len(self.data),len(other.data))):
            res=0
            if carry is not None:
                res=int(pointer.data)+int(carry)
            else:
                res=pointer.data
            res=str(res)
            if len(res)>1:
                carry=res[0]
                res=res[1]
            new_obj.add_first(res)
            pointer=pointer.prev
        if (carry is not None):
            if carry!='0':
                for i in range(len(carry)-1,-1,-1):
                    new_obj.add_first(carry[i])
        string="".join([elem for elem in new_obj])
        return Integer(string)
    def __mul__(self,other):
        new_obj=DoublyLinkedList()
        if len(self.data)<len(other.data):
            curr=self.data.trailer.prev
            curr_mul=other.data.trailer.prev
        else:
            curr=other.data.trailer.prev
            curr_mul=self.data.trailer.prev
        old=Integer('0')
        for i in range(min(len(self.data),len(other.data))):
            if len(self.data)<len(other.data):
                curr_mul=other.data.trailer.prev
            else:
                curr_mul=self.data.trailer.prev
            new_obj=DoublyLinkedList()
            carry=None
            for j in range(max(len(self.data),len(other.data))):
                res=0
                if carry is not None:
                    res=(int(curr.data)*int(curr_mul.data))+int(carry)
                else:
                    res=int(curr.data)*int(curr_mul.data)
                res=str(res)
                if len(res)>1:
                    carry=res[0]
                    res=res[1]
                else:
                    carry=None
                new_obj.add_first(res)
                curr_mul=curr_mul.prev
            if (carry is not None):
                if carry!='0':
                    for e in range(len(carry)-1,-1,-1):
                        new_obj.add_first(carry[e])
            for z in range(i):
                new_obj.add_last('0')
            if new_obj.is_empty()==False:
                string="".join([elem for elem in new_obj])
                add_obj=Integer(string)
                old=old+add_obj
            curr=curr.prev
        return old
                
    def __repr__(self):
        lst=[elem for elem in self.data]
        all_zero=0
        for i in range(len(lst)):
            if lst[i]=="0":
                all_zero+=1
        if all_zero==len(lst):
            return "0"
        else:
            first_non_zero=None
            continue_loop=True
            for j in range(len(lst)):
                if continue_loop==True:
                    if lst[j]!="0":
                        first_non_zero=j
                        continue_loop=False
            for j in range(first_non_zero):
                del lst[0]
            return "".join(lst)



