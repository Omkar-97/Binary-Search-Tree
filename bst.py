class Node:
    def __init__(self, value):
        self.right = self.left = None
        self.value = value

    def insert(self, data):
        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data > self.value:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def search(self, key):
        if key < self.value:
            if self.left is None:
                return str(key) + " not found"                
            return self.left.search(key)
        elif key > self.value:
            if self.right is None:
                return str(key) + " not found"                
            return self.right.search(key)
        else:
            return str(key) + " found"            

    def preorder(self):
        print(self.value, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value, end=" ")
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value, end=" ")


if __name__ == '__main__':
    import random
    tree_traversal = ["preorder", "inorder", "postorder"]
    node_list = random.sample(range(1, 20), 10)
    print("Nodes: {0}".format(node_list))
    search_list = random.sample(range(1, 20), 4)
    root_node = node_list.pop(0)
    print("Root-Node: {0}".format(root_node))
    tree = Node(root_node)
    for node in node_list:
        tree.insert(node)

    for traversal in tree_traversal:
        if traversal == "preorder":
            print()
            print("Pre-order Traversal")
            tree.preorder()
            print()
        if traversal == "inorder":
            print("In-order Traversal")
            tree.inorder()
            print()
        if traversal == "postorder":
            print("Post-order Traversal")
            tree.postorder()
            print()
            print()

    print("Search-list: {0}".format(search_list))
    for search in search_list:
        res = tree.search(search)
        print(res)
