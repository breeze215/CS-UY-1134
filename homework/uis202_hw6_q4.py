from DoublyLinkedList import *
def copy_linked_list(lnk_lst):
    n3=DoublyLinkedList()
    for elem in lnk_lst:
        n3.add_last(elem)
    return n3
def deep_copy_linked_list(lnk_lst):
    n3=DoublyLinkedList()
    curr=lnk_lst.header.next
    for i in range(len(lnk_lst)):
        if isinstance(curr.data,int):
            n3.add_last(curr.data)
        else:
            new=DoublyLinkedList()
            cursor=curr.data.header.next
            for i in range(len(curr.data)):
                if isinstance(cursor.data,int):
                    new.add_last(cursor.data)
                else:
                    new.add_last(deep_copy_linked_list(cursor.data))
                cursor=cursor.next
            n3.add_last(new)
        curr=curr.next
    return n3



                

