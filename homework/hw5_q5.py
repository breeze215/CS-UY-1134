from ArrayStack import *
from ArrayQueue import *
def permutations(lst):
    stack=ArrayStack()
    queue=ArrayQueue()
    final_lst=[]
    for elem in lst:
        stack.push(elem)
    length=len(stack)
    for i in range(length):
        if len(queue)==0:
            queue.enqueue([stack.pop()])
        else:
            length_two=len(queue)
            for i in range(length_two):
                var=queue.dequeue()
                for i in range(len(var)+1):
                    copy=var[:]
                    copy.insert(i,stack.top())
                    queue.enqueue(copy)
            stack.pop()
    for i in range(len(queue)):
        final_lst.append(queue.dequeue())
    return final_lst


        
    
    

        

        
