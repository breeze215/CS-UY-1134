from maps import *
from ArrayQueue import *
from LinkedBinaryTree import *

def min_max_BST(bst):
    min_max = (None, None)
    cursor = bst.root
    while(cursor is not None):
        min_max = (min_max[0], cursor.item.key)
        cursor = cursor.left
    cursor = bst.root
    while(cursor is not None):
        min_max = (cursor.item.key, min_max[1])
        cursor = cursor.left
    return min_max

def glt_n(bst, n):
    if(bst.is_empty()):
        raise Exception("Tree is empty")
    cursor = bst.root
    while(cursor is not None):
        if(cursor.data == n):
            return cursor.data
        elif (cursor.data < n):
            temp = cursor.data
            cursor = cursor.right
            if(cursor is None) and (temp < n):
                return temp
        else:
            temp = cursor.data
            cursor = cursor.left
            if(cursor is None) and (temp < n):
                return temp

def compare_BST(bst1, bst2):
    def compare_BST_helper(root, lst):
        q = ArrayQueue()
        q.enqueue(root)
        while(q):
            for _ in range(len(q)):
                node = q.dequeue()
                lst.append(node.data)
                if(node.right):
                    q.enqueue(node.right)
                if(node.left):
                    q.enqueue(node.left)
        return lst
    lst1 = []
    lst2 = []
    res_one = compare_BST_helper(bst1.root, lst1)
    res_two = compare_BST_helper(bst2.root, lst2)
    if len(res_one) != len(res_two):
        return False
    res_one.sort()
    res_two.sort()
    for i in range(len(res_one)):
        if(res_one[i] != res_two[i]):
            return False
    return True

def is_BST(root):
    return is_BST_helper(root)[2]
def is_BST_helper(root):
    if(root.left is None) and (root.right is None):
        return (root.data, root.data, True)
    if(root.left is not None) and (root.right is None):
        left = is_BST_helper(root.left)
        if left[1] < root.data:
            return (left[0], root.data, left[2])
        return (left[0], left[1], False)
    if(root.right is not None) and (root.left is None):
        right = is_BST_helper(root.right)
        if(right[0] > root.data):
            return (root.data, right[1], right[2])
        return (right[0], right[1], False)
    else:
        left = is_BST_helper(root.left)
        right = is_BST_helper(root.right)
        if(left[1] < root.data) and (right[0] > root.data):
            return (left[0], right[1], (left[2] and right[2]))
        return (left[0], right[0], False)


