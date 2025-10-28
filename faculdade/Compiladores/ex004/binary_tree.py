class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def put(self, item):
        self.items.append(item)

    def get(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("get from empty queue")


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def pre_order(self):
        print(self.value)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print(self.value)
        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.value)

    def bfs(self):
        queue = Queue()
        queue.put(self)

        while not queue.is_empty():
            current_node = queue.get()
            print(current_node.value, end=' ')
            if current_node.left_child:
                queue.put(current_node.left_child)
            if current_node.right_child:
                queue.put(current_node.right_child)
        print()

    def node_depth(self, node):
        if node is None:
            return 0
        left_depth = self.node_depth(node.left_child)
        right_depth = self.node_depth(node.right_child)
        return 1 + max(left_depth, right_depth)

class BinarySearchTree(BinaryTree):
    def __init__(self, value):
        super().__init__(value)

    def insert_node(self, value):
        if value <= self.value:
            if self.left_child:
                self.left_child.insert_node(value)
            else:
                self.left_child = BinarySearchTree(value)
        else:
            if self.right_child:
                self.right_child.insert_node(value)
            else:
                self.right_child = BinarySearchTree(value)

    def find_node(self, value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        elif value > self.value and self.right_child:
            return self.right_child.find_node(value)
        return value == self.value

    def find_minimum_value(self):
        if self.left_child:
            return self.left_child.find_minimum_value()
        else:
            return self.value

    def clear_node(self):
        self.value = None
        self.left_child = None
        self.right_child = None

    def remove_node(self, value, parent=None):
        if value < self.value and self.left_child:
            return self.left_child.remove_node(value, self)
        elif value > self.value and self.right_child:
            return self.right_child.remove_node(value, self)
        elif value == self.value:
            if self.left_child is None and self.right_child is None:
                if parent:
                    if parent.left_child == self:
                        parent.left_child = None
                    else:
                        parent.right_child = None
                self.clear_node()
            elif self.right_child is None:
                if parent:
                    if parent.left_child == self:
                        parent.left_child = self.left_child
                    else:
                        parent.right_child = self.left_child
                self.clear_node()
            elif self.left_child is None:
                if parent:
                    if parent.left_child == self:
                        parent.left_child = self.right_child
                    else:
                        parent.right_child = self.right_child
                self.clear_node()
            else:
                self.value = self.right_child.find_minimum_value()
                self.right_child.remove_node(self.value, self)
            return True
        return False

# ===================== TESTE =====================

bst = BinarySearchTree(10)
bst.insert_node(5)
bst.insert_node(15)
bst.insert_node(3)
bst.insert_node(7)
bst.insert_node(12)
bst.insert_node(18)

print("Profundidade da subárvore esquerda:", bst.node_depth(bst.left_child))
print("Contém 7?", bst.find_node(7))  # True
print("Contém 8?", bst.find_node(8))  # False
print("BFS:")
bst.bfs()  # 10 5 15 3 7 12 18
print("In-order:")
bst.in_order()  # 3 5 7 10 12 15 18
