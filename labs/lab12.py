from ArrayStack import *

from ArrayQueue import *

from LinkedBinaryTree import *

def is_perfect(root):

    if (root.left is None) and (root.right is None):

        return (True, 1)

    elif (root.left is None):

        prev = is_perfect(root.right)

        prev = (False, prev[1] + 1)

        return prev

    elif (root.right is None):

        prev = is_perfect(root.left)

        prev = (False, prev[1] + 1)

        return prev

    else:

        left_check = is_perfect(root.left)

        right_check = is_perfect(root.right)

        if (left_check[1] + 1 != right_check[1] + 1):

            return (False, min(left_check[1], right_check[1]))

        else:

            return (left_check[0] and right_check[0], left_check[1] + 1)

def is_perfect_iter(root):

    q = ArrayQueue()

    q.enqueue(root)

    level = 0

    while q.is_empty() == False:

        if len(q) != 2**level:

            return False

        else:

            for i in range(len(q)):

                node = q.dequeue()

                if (node.left is not None):

                    q.enqueue(node.left)

                if (node.right is not None):

                    q.enqueue(node.right)

            level += 1

    return True

def preorder_with_stack(self):

    stack = ArrayStack()

    stack.push(self.root)

    while len(stack) > 0:

        node = stack.pop()

        if (node.left is not None):

            stack.push(node.left)

        if (node.right is not None):

            stack.push(node.right)

        yield node.data

def invert_bt(root):

    if root is None:

        return

    left = invert_bt(root.left)

    right = invert_bt(root.right)

    root.left = right

    root.right = left

    return root

def invert_bt_iter(root):

    q = ArrayQueue()

    q.enqueue(root)

    while q.is_empty() == False:

        for i in range(len(q)):

            node = q.dequeue()

            left = node.left

            right = node.right

            node.left = right

            node.right = left

            if (left is not None):

                q.enqueue(left)

            if (right is not None):

                q.enqueue(right)

    return root


\
