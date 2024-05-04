from BinarySearchTreeMap import *

def create_chain_bst(n):
    tree = BinarySearchTreeMap()
    for i in range(1, n + 1):
        tree.insert(i, None)
    return tree

def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

def add_items(bst, low, high):
    if(low == high):
        mid = (low + high) // 2
        bst.insert(mid, None)
        return
    else:
        mid = (low + high) // 2
        bst.insert(mid, None)
        left_tree = add_items(bst, low, mid - 1)
        right_tree = add_items(bst, mid + 1, high)


