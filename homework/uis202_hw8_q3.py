from BinarySearchTreeMap import *

def restore_bst(prefix_lst):
    tree = BinarySearchTreeMap()
    def restore_bst_helper(prefix_lst, upper_bound):
        if(not prefix_lst) or (prefix_lst[-1] > upper_bound):
            return None
        item = tree.Item(prefix_lst.pop())
        node = tree.Node(item)
        node.left = restore_bst_helper(prefix_lst, item.key)
        node.right = restore_bst_helper(prefix_lst, upper_bound)
        return node
    tree.root = restore_bst_helper(prefix_lst[::-1], float('inf'))
    tree.n = len(prefix_lst)
    return tree
    

                      
        
        
        
        
        
        
        
