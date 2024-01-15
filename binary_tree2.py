class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self,root):
        self.root = Node(root)


    def post_order (self, start , records):
        if start is not None:
            records = self.post_order(start.left,records)
            records = self.post_order(start.right , records)
            records.append(start.value)

        return records


tree = Tree(5)
tree.root.left = Node(3)
tree.root.right = Node(4)
tree.root.left.left = Node(2)
tree.root.left.right = Node(8)

print(tree.post_order(tree.root , []))

