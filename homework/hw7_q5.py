from LinkedBinaryTree import *

def create_expression_tree(prefix_exp_str):

    def create_expression_tree_helper(prefix_exp, start_pos):

        if (start_pos >= len(prefix_exp)):

            return

        if(prefix_exp[start_pos] not in '*+/-'):

            create_expression_tree_helper(prefix_exp, start_pos + 1)

            return (LinkedBinaryTree.Node(int(prefix_exp[start_pos])), start_pos + 1)

        left_node_of_tree = create_expression_tree_helper(prefix_exp, start_pos + 1)

        right_node_of_tree = create_expression_tree_helper(prefix_exp, left_node_of_tree[1]) 

        return (LinkedBinaryTree.Node(prefix_exp[start_pos], left_node_of_tree[0], right_node_of_tree[0]), right_node_of_tree[1])

    prefix_exp = prefix_exp_str.split(" ")

    return LinkedBinaryTree(create_expression_tree_helper(prefix_exp, 0)[0])

def prefix_to_postfix(prefix_exp_str):

    return " ".join(str(elem.data) for elem in (create_expression_tree(prefix_exp_str)).postorder())
                       

            

            

    

            

        

        

        

        

        
        
