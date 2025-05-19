import csv
class Node:
    def __init__(self, key):
        self.key = key  # key should be a tuple like (id, name, password)
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        if key[0] < root.key[0]:  # Assuming unique ID as key
            root.left = self._insert_recursive(root.left, key)
        else:
            root.right = self._insert_recursive(root.right, key)
        return root

    def search_name(self, key_tuple):
        return self._search_name(self.root, key_tuple)

    def _search_name(self, root, key_tuple):
        if not root:
            return None
        if root.key[0] == key_tuple[0] and root.key[2] == key_tuple[1]:
            return root.key
        elif key_tuple[0] < root.key[0]:
            return self._search_name(root.left, key_tuple)
        else:
            return self._search_name(root.right, key_tuple)

    def inorder_traversal(self, root):
        if root is None:
            return []
        return self.inorder_traversal(root.left) + [root.key] + self.inorder_traversal(root.right)

    def _construct_bst_from_csv(self, filename):
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = [ (int(row[0]), row[1], row[2]) for row in reader ]

        # Sort by ID before building balanced BST
        data.sort(key=lambda x: x[0])
        self.root = self.list_to_bst(data)
        return self.root

    def list_to_bst(self, lst):
        if not lst:
            return None
        mid = len(lst) // 2
        node = Node(lst[mid])
        node.left = self.list_to_bst(lst[:mid])
        node.right = self.list_to_bst(lst[mid+1:])
        return node

    def store_bst_data_to_csv(self, filename):
        data = self.inorder_traversal(self.root)
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
