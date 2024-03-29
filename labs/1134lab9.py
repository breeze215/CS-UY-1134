from ArrayStack import *
def eval_prefix(exp_str):
    s=ArrayStack()
    exp_lst=exp_str.split(" ")
    char="-+*/"
    for i in range(len(exp_lst)-1,-1,-1):
        elem=exp_lst[i]
        if elem not in char:
            s.push(int(elem))
        else:
            value2=s.pop()
            value1=s.pop()
            if elem=="-":
                val=value1-value2
                s.push(val)
            elif elem=="+":
                val=value1+value2
                s.push(val)
            elif elem=="/":
                if value2==0:
                    raise ZeroError("cannot divide by 0")
                else:
                    val=value1//value2
                    s.push(val)
            else:
                val=value1*value2
                s.push(val)
    return s.pop()
class ArrayDeque:
    initial_capacity=0
    def __init__(self):
        self.data=make_array(ArrayDeque.initial_capacity)
        self.n=0
        self.front_ind,self.back_ind=None,None
    def __len__(self):
        return self.n
    def is_empty(self):
        return (self.n==0)
    def enqueue_first(self,elem):
        if self.n==len(self.data):
            self.resize(2*len(self.data))
        if self.is_empty():
            self.data[0]=elem
            self.front_ind,self.back_ind=0,0
            self.n=1
        else:
            self.front_ind=(self.front_ind-1)%len(self.data)
            self.data[self.front_ind]=elem
            self.n+=1
    def enqueue_last(self,elem):
        if self.n==len(self.data):
            self.resize(2*len(self.data))
        if self.is_empty():
            self.data[0]=elem
            self.front_ind,self.back_ind=0,0
            self.n=1
        else:
            self.back_ind=(self.back_ind+1)%len(self.data)
            self.data[self.back_ind]=elem
            self.n+=1
    def dequeue_first(self):
        if self.is_empty():
            raise Exception("queue is empty")
        else:
            value=self.data[self.front_ind]
            self.data[self.front_ind]=None
            self.front_ind=(self.front_ind+1)%len(self.data)
            self.n-=1
            if self.is_empty():
                self.front_ind,self.back_ind=None,None
            elif self.n<(len(self.data)//4):
                self.resize(len(self.data)//2)
            return value
    def dequeue_last(self):
        if self.is_empty():
            raise Exception("queue is empty")
        else:
            value=self.data[self.back_ind]
            self.data[self.back_ind]=None
            self.back_ind=(self.back_ind-1)%len(self.data)
            self.n-=1
            if self.is_empty():
                self.front_ind,self.back_ind=None,None
            elif self.n<(len(self.data)//4):
                self.resize(len(self.data)//2)
            return value
    def front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front_ind]
    def last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.back_ind]
def flatten_list_by_depth(lst):
    q=ArrayQueue()
    new_lst=[]
    for elem in lst:
        q.enqueue(elem)
    while q.is_empty()==False:
        length=len(q)
        for i in range(length):
            front=q.dequeue()
            if isinstance(front,list):
                for elem in front:
                    q.enqueue(elem)
            elif isinstance(front,int):
                new_lst.append(front)
    return new_lst
