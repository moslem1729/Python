import sys
from python.DataStructures.BST import Tree 


def validate_binary_search_tree(tree):
    return validate_binary_search_tree_helper(tree.root,float("-inf"),float("inf"))
        

def validate_binary_search_tree_helper(node,min_value,max_value):
    if node is None:
        return True
    if node.data<min_value or node.data>max_value:
        return False
    left_is_valid=validate_binary_search_tree_helper(node.leftChild,min_value,node.data)
    return left_is_valid and validate_binary_search_tree_helper(node.rightChild,node.data,max_value)


print(sys.path)

tree = Tree()
tree.insert(5)
tree.insert(7)
tree.root.rightChild.data = 4
tree.insert(8)
tree.insert(4)
tree.inorder()
print(validate_binary_search_tree(tree))