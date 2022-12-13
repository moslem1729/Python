from python.DataStructures.BST import Tree


def min_height_bst(array):
    tree = Tree()
    min_height_bst_helper(tree, array)
    print_tree(tree.root)


def min_height_bst_helper(tree, array):
    left = 0
    right = len(array)
    mid = (left + right) // 2
    if len(array) == 0:
        return
    elif len(array) == 1:
        tree.insert(array[0])
        return
    else:
        tree.insert(array[mid])
        min_height_bst_helper(tree, array[mid + 1:right])
        min_height_bst_helper(tree, array[left:mid])


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.leftChild, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.data))
        print_tree(node.rightChild, level + 1)


array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
min_height_bst(array)
