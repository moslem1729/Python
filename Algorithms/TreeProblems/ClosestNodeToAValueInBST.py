from DataStructures.BST import Tree ,Node

tree=Tree()
tree.insert(10)
tree.insert(15)
tree.insert(13)
tree.insert(22)
tree.insert(14)
tree.insert(5)
tree.insert(2)
tree.insert(5)
tree.insert(1)

def closest_number(node,number,current_closest_node):
    currentdif=node.data-number
    if currentdif<0:
        if node.rightChild is None:
            if abs(node.data - number) < abs(current_closest_node.data - number):
                return node.dat
            else :
                return current_closest_node.data
        else:
            if abs(node.data-number)<abs(current_closest_node.data-number):
                return closest_number(node.rightChild,number,node)
            else:
                return closest_number(node.rightChild,number,current_closest_node)
    elif currentdif>0:
        if node.leftChild is None:
            if abs(node.data - number) < abs(current_closest_node.data - number):
                return node.data
            if abs(node.data - number) > abs(current_closest_node.data - number):
                return current_closest_node.data
        else:
            if abs(node.data - number) < abs(current_closest_node.data - number):
                return closest_number(node.leftChild, number, node)
            else:
                return closest_number(node.leftChild, number, current_closest_node)
    else:
        return node.data




print(tree.root.data)
print(closest_number(tree.root,12,tree.root))










