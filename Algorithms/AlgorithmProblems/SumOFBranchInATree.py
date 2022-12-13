from DataStructures.BST import Tree

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


def branch_sums(root):
    sums = []
    calculate_branch_sums(root, 0, sums)
    return sums


def calculate_branch_sums(node, running_sum, sums):
    if node is None:
        return
    
    new_running_sum=running_sum+node.data

    if node.leftChild is None and node.rightChild is None:
        sums.append(new_running_sum)
        return

    calculate_branch_sums(node.leftChild,new_running_sum,sums)
    calculate_branch_sums(node.rightChild,new_running_sum,sums)


# def branch_sums_nested_functions(root):
#     sum=0
#     sums=[]
#     running_sum=0
#     def calculate_branch_sums_nested_function(node,running_sum):
#         if node is None:
#             nonlocal sums
#             sums.append(sum)
#
#             return
#         nonlocal sum
#         new_running_sum=running_sum+node.data
#         sum=sum+new_running_sum
#         calculate_branch_sums_nested_function(node.rightChild,new_running_sum)
#         calculate_branch_sums_nested_function(node.leftChild,new_running_sum)
#
#     calculate_branch_sums_nested_function(root,running_sum)
#     return sum
#

print(branch_sums(tree.root))
# print(branch_sums_nested_functions(tree.root))
tree.preorder()
