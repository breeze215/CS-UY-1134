
import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()
class ArrayList:
    def __init__(self):
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0

    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity = new_size

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)


    def __getitem__(self, ind):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        return self.data[ind]

    def __setitem__(self, ind, val):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        self.data[ind] = val


    def __repr__(self):
        data_as_strings = [str(self.data[i]) for i in range(self.n)]
        return '[' + ', '.join(data_as_strings) + ']'


    def __add__(self, other):
        res = ArrayList()
        res.extend(self)
        res.extend(other)
        return res

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __mul__(self, times):
        res = ArrayList()
        for i in range(times):
            res.extend(self)
        return res

    def __rmul__(self, times):
        return self * times



class StaticArrayStack:
    def __init__(self, max_capacity):
        self.data = make_array(max_capacity)
        self.capacity = max_capacity
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def is_full(self):
        return (len(self) == self.capacity)

    def push(self, item):
        if(self.is_full()):
            raise Exception("Stack is full")
        self.data[self.n] = item
        self.n += 1

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        item = self.data[self.n - 1]
        self.data[self.n - 1] = None
        self.n -= 1
        return item

    def top(self):
        if(self.is_empty()):
            raise Exception("Stack is empty")
        return self.data[self.n - 1]

class ArrayStack:
    def __init__(self):
        self.data = ArrayList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data.pop()
class MaxStack:
    def __init__(self):
        self.data=make_array(4)
        self.highest_elem=None
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return (self.len==0)
    def push(self,val):
        if self.is_empty():
            self.highest_elem=val
            self.data.append(val)
        else:
            self.data.append(val)
            if val>self.highest_elem:
                self.highest_elem=val
    def top(self):
        if self.is_empty():
            raise Exception("stack is empty")
        else:
            return self.data[-1]
    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty")
        else:
            return self.data.pop()
    def max(self):
        if self.is_empty():
            raise Exception("stack is empty")
        else:
            return self.highest_elem

class StaticArrayQueue:
    def __init__(self, max_cap):
        self.data_arr = make_array(max_cap)
        self.capacity = max_cap
        self.n = 0
        self.front_ind = None

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def is_full(self):
        return (self.n == self.capacity)

    def enqueue(self, item):
        if(self.is_full()):
            raise Exception("Queue is full")
        elif(self.is_empty()):
            self.data_arr[0] = item
            self.front_ind = 0
            self.n += 1
        else:
            back_ind = (self.front_ind + self.n) % self.capacity
            self.data_arr[back_ind] = item
            self.n += 1

    def dequeue(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % self.capacity
        self.n -= 1
        if(self.is_empty()):
            self.front_ind = None
        return value

    def first(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        return self.data_arr[self.front_ind]




class ArrayQueue:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data_arr = make_array(ArrayQueue.INITIAL_CAPACITY)
        self.capacity = ArrayQueue.INITIAL_CAPACITY
        self.n = 0
        self.front_ind = None

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, elem):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        if (self.is_empty()):
            self.data_arr[0] = elem
            self.front_ind = 0
            self.n += 1
        else:
            back_ind = (self.front_ind + self.n) % self.capacity
            self.data_arr[back_ind] = elem
            self.n += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % self.capacity
        self.n -= 1
        if(self.is_empty()):
            self.front_ind = None
        if((self.n < self.capacity // 4) and
                (self.capacity > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(self.capacity // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data_arr[self.front_ind]

    def resize(self, new_cap):
        new_data = make_array(new_cap)
        old_ind = self.front_ind
        for new_ind in range(self.n):
            new_data[new_ind] = self.data_arr[old_ind]
            old_ind = (old_ind + 1) % self.capacity
        self.data_arr = new_data
        self.capacity = new_cap
        self.front_ind = 0


class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            if (left is not None):
                self.left.parent = self
            self.right = right
            if (right is not None):
                self.right.parent = self
            self.parent = None


    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes()

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)


    def count_nodes(self):
        def subtree_count(root):
            if(root is None):
                return 0
            else:
                left_count = subtree_count(root.left)
                right_count = subtree_count(root.right)
                return left_count + right_count + 1

        return subtree_count(self.root)


    def sum(self):
        def subtree_sum(root):
            if(root is None):
                return 0
            else:
                left_sum = subtree_sum(root.left)
                right_sum = subtree_sum(root.right)
                return left_sum + right_sum + root.data

        return subtree_sum(self.root)

    def height(self):
        def subtree_height(root):
            if((root.left is None) and (root.right is None)):
                return 0
            elif(root.right is None): #left is not None
                left_height = subtree_height(root.left)
                return 1 + left_height
            elif(root.left is None): #right is not None
                right_height = subtree_height(root.right)
                return 1 + right_height
            else: #both subtrees are not None
                left_height = subtree_height(root.left)
                right_height = subtree_height(root.right)
                return 1 + max(left_height, right_height)

        if(self.is_empty()):
            raise Exception("Tree is empty")
        return subtree_height(self.root)


    def preorder(self):
        def subtree_preorder(root):
            if(root is None):
                pass
            else:
                yield root
                yield from subtree_preorder(root.left)
                yield from subtree_preorder(root.right)

        yield from subtree_preorder(self.root)


    def inorder(self):
        def subtree_inorder(root):
            if(root is None):
                pass
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)


    def postorder(self):
        def subtree_postorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_postorder(root.left)
                yield from subtree_postorder(root.right)
                yield root

        yield from subtree_postorder(self.root)


    def breadth_first(self):
        if(self.is_empty()):
            return
        bfs_queue = ArrayQueue()
        bfs_queue.enqueue(self.root)
        while(bfs_queue.is_empty() == False):
            curr_node = bfs_queue.dequeue()
            yield curr_node
            if(curr_node.left is not None):
                bfs_queue.enqueue(curr_node.left)
            if(curr_node.right is not None):
                bfs_queue.enqueue(curr_node.right)


    def __iter__(self):
        for node in self.inorder():
            yield node.data

    def preorder_with_stack(self):
        ''' Returns a generator function that iterates through
        the tree using the preorder traversal '''
        stack = ArrayStack()
        stack.push(self.root)
        while(len(stack) > 0):
            node = stack.pop()
            if(node.right is not None):
                stack.push(node.right)
            if(node.left is not None):
                stack.push(node.left)
            yield node.data
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

    def iterative_inorder(self):

        curr = self.root

        while(curr is not None):

            if(curr.left is None):

                yield curr.data

                curr = curr.right

            else:

                res = curr.left

                while(res.right is not None) and (res.right != curr):

                    res = res.right

                if(res.right is None):

                    res.right = curr

                    curr = curr.left

                else:

                    res.right = None

                    yield curr.data

                    curr = curr.right
                        
