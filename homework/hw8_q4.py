from BinarySearchTreeMap import *

def find_min_abs_difference(bst):
    def find_diff_helper(root, prev_val, diff):
        if(root is not None):
            prev_val, diff = find_diff_helper(root.left, prev_val, diff)
            prev_val, diff = root.item.key, min(abs(root.item.key - prev_val), diff)
            prev_val, diff = find_diff_helper(root.right, prev_val, diff)
        return prev_val, diff
    if(bst.root is None):
        raise Exception("no absolute difference on empty trees")
    if(bst.root.left is None) and (bst.root.right is None):
        raise Exception("no absolute difference on trees containing one node")
    prev_val, diff = find_diff_helper(bst.root, float('-inf'), float('inf'))
    return diff
     


