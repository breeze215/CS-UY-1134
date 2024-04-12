def bt_even_sum(root):
        def bt_subtree_even_sum(root):
            if (root.left is None) and (root.right is None):
                if root.data%2==0:
                    return root.data
                else:
                    return 0
            elif (root.right is None):
                left_sum=bt_subtree_even_sum(root.left)
                if root.data%2==0:
                    return root.data+left_sum
                else:
                    return left_sum
            elif (root.left is None):
                right_sum=bt_subtree_even_sum(root.right)
                if root.data%2==0:
                    return root.data+right_sum
                else:
                    return right_sum
            else:
                left_sum=bt_subtree_even_sum(root.left)
                right_sum=bt_subtree_even_sum(root.right)
                if root.data%2==0:
                    return root.data+left_sum+right_sum
                else:
                    return left_sum+right_sum
        if root is None:
            raise Exception("Tree is empty")
        else:
            return bt_subtree_even_sum(root)
def is_full(root):
    def is_full_subtree(root):
        if (root.left is None) and (root.right is None):
            return True
        elif (root.left is None):
            right_check=is_full_subtree(root.right)
            return False and right_check
        elif (root.right is None):
            left_check=is_full_subtree(root.left)
            return False and left_check
        else:
            left_check=is_full_subtree(root.left)
            right_check=is_full_subtree(root.right)
            return True and left_check and right_check
    if root is None:
        raise Exception("tree is empty")
    else:
        return is_full_subtree(root)
 def __contains__(self, item):
        def contains_subtree(root):
            if (root.left is None) and (root.right is None):
                return False
            elif (root.left is None):
                right_check=contains_subtree(root.right)
                if root.data is item:
                    return True or right_check
                else:
                    return False or right_check
            elif (root.right is None):
                left_check=contains_subtree(root.left)
                if root.data is item:
                    return True or left_check
                else:
                    return False or left_check
            else:
                left_check=contains_subtree(root.left)
                right_check=contains_subtree(root.right)
                if root.data is item:
                    return True or left_check or right_check
                else:
                    return False or left_check or right_check
        if self.is_empty():
            raise Exception("tree is empty")
        else:
            return contains_subtree(self.root)
 def __add__(self, other):
        def merge(t1,t2):
            if t1 is not None and t2 is not None:
                res=t1.data+t2.data
                new_left=merge(t1.left,t2.left)
                new_right=merge(t1.right,t2.right)
                return LinkedBinaryTree.Node(res,new_left,new_right)
            elif t1 is not None:
                new_left=merge(t1.data,None)
                new_right=merge(t1.right,None)
                return LinkedBinaryTree.Node(t1.data,new_left,new_right)
            elif t2 is not None:
                new_left=merge(None,t2.left)
                new_right=merge(None,t2.right)
                return LinkedBinaryTree.Node(t2.data,new_left,new_right)
            else:
                return None
        new_root=merge(self.root,other.root)
        return LinkedBinaryTree(new_root)

