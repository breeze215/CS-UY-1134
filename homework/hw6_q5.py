from DoublyLinkedList import *

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):

    def merge_sublists(curr_one, curr_two, dl):
        
        if (curr_one.data is None) and (curr_two.data is None):

            return dl
        
        else:
            if curr_one.data is not None and curr_two.data is None:

                dl.add_last(curr_one.data)

                return merge_sublists(curr_one.next, curr_two, dl)

            if curr_one.data is None and curr_two.data is not None:

                dl.add_last(curr_two.data)
                
                return merge_sublists(curr_one, curr_two.next, dl)
            

            if curr_one.data>curr_two.data:

                dl.add_last(curr_two.data)
                
                return merge_sublists(curr_one, curr_two.next, dl)
                
            elif curr_one.data<curr_two.data:
 
                dl.add_last(curr_one.data)
                
                return merge_sublists(curr_one.next, curr_two, dl)
                
            else:
                
                dl.add_last(curr_one.data)

                dl.add_last(curr_two.data)
                
                return merge_sublists(curr_one.next, curr_two.next, dl)
                
    return merge_sublists(srt_lnk_lst1.header.next,srt_lnk_lst2.header.next, DoublyLinkedList())


            
            
        
        
