class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def insert(self, data):
        child = TreeNode(data)
        child.parent = self
        self.children.append(child)

    def depth_first_search(self, array=None):
        if array is None:
            array = []
        if len(self.children) == 0:
            array.append(self.data)
            return
        else:
            array.append(self.data)
            for i in self.children:
                i.depth_first_search(array)
        return array

    def depths_of_node(self, depths=1):
        if self.parent is not None:
            depths = depths + 1
            return self.parent.depths_of_node(depths)
        else:
            return depths

    def print_tree(self):
        if len(self.children) > 0:
            print(self.depths_of_node() * "_", self.data)
            for i in self.children:
                i.print_tree()
        else:
            print(self.depths_of_node() * "_", self.data)


n = TreeNode("A")
n.insert("B")
n.insert("C")
n.insert("D")
n.children[0].insert("E")
n.children[0].insert("F")
n.children[0].children[0].insert("P")
n.children[0].children[1].insert("I")
n.children[0].children[1].insert("J")
n.children[2].insert("G")
n.children[2].children[0].insert("K")
n.children[2].insert("H")
print(n.depth_first_search())
n.print_tree()
