from ...DataStructures.BST import Tree

tree = Tree()

tree.insert(10)
tree.insert(15)
tree.insert(13)
tree.insert(22)
tree.insert(14)
tree.insert(5)
tree.insert(2)
tree.insert(5)
tree.insert(1)


def node_depths(root):
    node_depths = 0
    flag = 0

    def calculate_node_depths(node, flag):
        if node is None:
            return

        nonlocal node_depths
        node_depths = node_depths + flag
        flag = flag + 1
        calculate_node_depths(node.leftChild, flag)
        calculate_node_depths(node.rightChild, flag)

    calculate_node_depths(root, flag)

    return node_depths


def node_depths_recursion(root):
    current_node_depth = 0
    node_depths = calculate_node_depths_recursion(root, current_node_depth)
    return node_depths


def calculate_node_depths_recursion(node, current_depths):
    if node is None:
        return 0
    return calculate_node_depths_recursion(node.leftChild, current_depths + 1) + calculate_node_depths_recursion(
        node.rightChild, current_depths + 1) + current_depths


def node_depths_iteration(root):
    node_depths = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        node_info = stack.pop()
        node, depth = node_info["node"], node_info["depth"]
        if node is None:
            continue
        node_depths += depth
        stack.append({"node": node.leftChild, "depth": depth + 1})
        stack.append({"node": node.rightChild, "depth": depth + 1})
    return node_depths


print(node_depths_iteration(tree.root))
print(node_depths_recursion(tree.root))
print(node_depths(tree.root))

tree.preorder()
