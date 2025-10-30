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
        self.height = 1  # garantir que todo nó tenha height, evita inconsistências

    def pre_order(self):
        result = [self.value]
        if self.left_child:
            result += self.left_child.pre_order()
        if self.right_child:
            result += self.right_child.pre_order()
        return result

    def in_order(self):
        result = []
        if self.left_child:
            result += self.left_child.in_order()
        result.append(self.value)
        if self.right_child:
            result += self.right_child.in_order()
        return result

    def post_order(self):
        result = []
        if self.left_child:
            result += self.left_child.post_order()
        if self.right_child:
            result += self.right_child.post_order()
        result.append(self.value)
        return result

    def bfs(self):
        queue = Queue()
        queue.put(self)
        result = []
        while not queue.is_empty():
            current_node = queue.get()
            result.append(current_node.value)
            if current_node.left_child:
                queue.put(current_node.left_child)
            if current_node.right_child:
                queue.put(current_node.right_child)
        return result

    def node_depth(self, node):
        if node is None:
            return 0
        left_depth = self.node_depth(node.left_child)
        right_depth = self.node_depth(node.right_child)
        return 1 + max(left_depth, right_depth)


class BinarySearchTree(BinaryTree):
    def __init__(self, value, ignore_duplicates=True):
        super().__init__(value)
        self.ignore_duplicates = ignore_duplicates

    def get_height(self, node):
        if node is None:
            return 0
        return getattr(node, 'height', 1)

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.right_child) - self.get_height(node.left_child)

    def rotate_left(self, z):
        y = z.right_child
        T2 = y.left_child
        y.left_child = z
        z.right_child = T2
        self.update_height(z)
        self.update_height(y)
        return y

    def rotate_right(self, z):
        y = z.left_child
        T3 = y.right_child
        y.right_child = z
        z.left_child = T3
        self.update_height(z)
        self.update_height(y)
        return y

    def _rebalance_node(self, node):
        if node is None:
            return None
        self.update_height(node)
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.right_child) >= 0:
            return self.rotate_left(node)
        if balance > 1 and self.get_balance(node.right_child) < 0:
            node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)
        if balance < -1 and self.get_balance(node.left_child) <= 0:
            return self.rotate_right(node)
        if balance < -1 and self.get_balance(node.left_child) > 0:
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)
        return node

    def balance_tree(self, node=None):
        """Rebalanceia a subárvore cuja raiz é `node` e retorna a nova raiz dessa subárvore.

        Se chamado sem argumento, rebalanceia a árvore inteira e retorna a nova raiz.
        """
        if node is None:
            node = self
        if node is None:
            return None

        # recursão post-order para garantir que filhos estejam balanceados antes do pai
        if node.left_child:
            node.left_child = self.balance_tree(node.left_child)
        if node.right_child:
            node.right_child = self.balance_tree(node.right_child)

        return self._rebalance_node(node)

    def insert_node(self, value):
        # insere e obtém a nova raiz da subárvore (pode mudar)
        new_root = self._insert_node(self, value)
        # aplica nova raiz à instância atual (preserva referência externa)
        if new_root:
            self.value = new_root.value
            self.left_child = new_root.left_child
            self.right_child = new_root.right_child
            self.height = getattr(new_root, 'height', 1)

    def _insert_node(self, node, value):
        if node is None:
            return BinarySearchTree(value, ignore_duplicates=self.ignore_duplicates)

        if value == node.value:
            if self.ignore_duplicates:
                return node
            else:
                node.value = value
                return node

        if value < node.value:
            node.left_child = self._insert_node(node.left_child, value)
        else:
            node.right_child = self._insert_node(node.right_child, value)

        return self._rebalance_node(node)

    def insert_many(self, values):
        for v in values:
            self.insert_node(v)

    def find_min_value_node(self, node):
        current = node
        while current.left_child:
            current = current.left_child
        return current

    def remove_node(self, value):
        new_root = self._remove_node(self, value)
        if new_root:
            self.value = new_root.value
            self.left_child = new_root.left_child
            self.right_child = new_root.right_child
            self.height = getattr(new_root, 'height', 1)
        else:
            # árvore ficou vazia
            self.value = None
            self.left_child = None
            self.right_child = None
            self.height = 1

    def _remove_node(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left_child = self._remove_node(node.left_child, value)
        elif value > node.value:
            node.right_child = self._remove_node(node.right_child, value)
        else:
            if node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child

            temp = self.find_min_value_node(node.right_child)
            node.value = temp.value
            node.right_child = self._remove_node(node.right_child, temp.value)

        return self._rebalance_node(node)

    def is_balanced(self, node=None):
        if node is None:
            node = self

        if node is None:
            return True

        left_height = self.get_height(node.left_child)
        right_height = self.get_height(node.right_child)

        if abs(left_height - right_height) > 1:
            return False

        left_ok = True
        right_ok = True

        if node.left_child:
            left_ok = self.is_balanced(node.left_child)
        if node.right_child:
            right_ok = self.is_balanced(node.right_child)

        return left_ok and right_ok

    def pretty_print(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self
        print("    " * level + prefix + str(node.value))
        if node.left_child:
            self.pretty_print(node.left_child, level + 1, prefix="L--- ")
        if node.right_child:
            self.pretty_print(node.right_child, level + 1, prefix="R--- ")


# ============= TESTE =============

bst = BinarySearchTree(10)
vals = [5, 15, 3, 7, 12, 18, 1, 8]
bst.insert_many(vals)

print("In-order:", bst.in_order())
print("Pré-order:", bst.pre_order())
print("Pós-order:", bst.post_order())
print("BFS antes do balanceamento explícito:", bst.bfs())
print("Árvore balanceada?", bst.is_balanced())
print("\nVisualização antes do balanceamento:")
bst.pretty_print()

# balanceia explicitamente e aplica a nova raiz
bst.insert_node(2)
new_root = bst.balance_tree()

print("\nBFS após balanceamento explícito:", new_root.bfs())

new_root.remove_node(3)
new_root.remove_node(15)
print("Visualização após apagar e rebalancear nós:")
new_root.balance_tree().pretty_print()