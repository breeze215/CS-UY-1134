from LinkedBinaryTree import *

def is_height_balanced(bin_tree):

    def is_height_balanced_subtree(root):

        if (root.left is None) and (root.right is None):
            
            return (True, 1)

        elif (root.left is None) and (root.right is not None):

            right_check = is_height_balanced_subtree(root.left)

            if (right_check[1] - 1 != 0):

                right_check = (False, right_check[1] + 1)

            return right_check

        elif (root.right is None) and (root.left is not None):

            left_check = is_height_balanced_subtree(root.left)

            if (left_check[1] - 1 != 0):

                left_check = (False, left_check[1] + 1)

            return left_check

        else:

            left_check = is_height_balanced_subtree(root.left)

            right_check = is_height_balanced_subtree(root.right)

            return (left_check[0] and right_check[0], 1  + max(left_check[1], right_check[1]))

    if (bin_tree.root is None):

        return True

    return is_height_balanced_subtree(bin_tree.root)[0]


