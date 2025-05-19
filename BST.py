import csv
class TreeNode:
    def __init__(self, key,name,passkey):
        self.key = key
        self.name= name
        self.passkey=passkey
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key,name,passkey):
        self.root = self._insert(self.root,key,name,passkey)

    def _insert(self,root, key, name, passkey):
        if root is None:
           return TreeNode(key, name, passkey)
        if key < root.key:
            root.left = self._insert(root.left, key, name, passkey)
        else:
            root.right = self._insert(root.right, key, name, passkey)
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    
    def search_name(self, key, passkey):
        return self._search_name(self.root, key, passkey)

    def _search_name(self, node, key, passkey):
        if node is None or node.key == key and node.passkey == passkey:
            return node
        if key < node.key:
            return self._search_name(node.left, key, passkey)
        return self._search_name(node.right, key, passkey)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append([node.key,node.name,node.passkey])
            self._inorder_traversal(node.right, result)

    def store_bst_data_to_csv(self):
        result = self.inorder_traversal()
        with open("data.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for data in result:
                writer.writerow(data)
        
        
    def contruct_bst_from_csv(self):
        return self._construct_bst_from_csv("data.csv")
    def _construct_bst_from_csv(self,filename):
        root = None
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 3:
                    root = self.insert(int(row[0]), row[1], row[2])
                else:
                    pass
        return root
    def delete(self, key, passkey):
        self.root = self._delete(self.root, key, passkey)

    def _delete(self, node, key, passkey):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key, passkey)
        elif key > node.key:
            node.right = self._delete(node.right, key, passkey)
        else:
            
            if node.passkey != passkey:
                print("Passkey does not match. Node not deleted.")
                return node

        
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            
            successor = self._min_value_node(node.right)
            
            node.key = successor.key
            node.name = successor.name
            node.passkey = successor.passkey
            
            node.right = self._delete(node.right, successor.key, successor.passkey)

        return node
    def _min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left
        return current
