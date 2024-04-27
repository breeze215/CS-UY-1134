from LinkedBinaryTree import *

def min_and_max(bin_tree):

    def subtree_min_and_max(root):

        if (root.left is None) and (root.right is None):

            return (root.data, root.data)
            
        elif (root.left is None) and (root.right is not None):

            min_and_max_tuple = subtree_min_and_max(root.right)
                
            if root.right.data < min_and_max_tuple[0]:

                min_and_max_tuple = (root.right.data, min_and_max_tuple[1])

            if root.right.data > min_and_max_tuple[1]:

                min_and_max_tuple = (min_and_max_tuple[0], root.right.data)

            return min_and_max_tuple

        elif (root.right is None) and (root.left is not None):

            min_and_max_tuple = subtree_min_and_max(root.left)

            if root.left.data < min_and_max_tuple[0]:

                min_and_max_tuple = (root.left.data, min_and_max_tuple[1])

            if root.left.data > min_and_max_tuple[1]:

                min_and_max_tuple = (min_and_max_tuple[0], root.left.data)

            return min_and_max_tuple

        else:

            min_and_max_tuple_one = subtree_min_and_max(root.left)

            min_and_max_tuple_two = subtree_min_and_max(root.right)

            if (min_and_max_tuple_one[0] < min_and_max_tuple_two[0]) and (min_and_max_tuple_one[1] > min_and_max_tuple_two[1]): 

                return min_and_max_tuple_one

            else:

                return min_and_max_tuple_two

    if (bin_tree.root is None):

        raise Exception("Tree is empty")
        
    return subtree_min_and_max(bin_tree.root)



