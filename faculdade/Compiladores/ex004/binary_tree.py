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


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


def getHeight(node):
    if not node:
        return 0
    return node.height


def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)


def rightRotate(y):
    print('Rotate right on node', y.data)
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    return x


def leftRotate(x):
    print('Rotate left on node', x.data)
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return y


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def insert(node, data):
    if not node:
        return TreeNode(data)

    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)

    # Update the balance factor and balance the tree
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)

    # Balancing the tree
    # Left Left
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)

    # Left Right
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)

    # Right Right
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)

    # Right Left
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node


def delete(node, data):
    if not node:
        return node

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        temp = minValueNode(node.right)
        node.data = temp.data
        node.right = delete(node.right, temp.data)

    if node is None:
        return node

    # Update the balance factor and balance the tree
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)

    # Balancing the tree
    # Left Left
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)

    # Left Right
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)

    # Right Right
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)

    # Right Left
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node


def preOrderTraversal(node):
    result = [node.data]
    if node.left:
        result += preOrderTraversal(node.left)
    if node.right:
        result += preOrderTraversal(node.right)
    return result


def inOrderTraversal(node):
    result = []
    if node.left:
        result += inOrderTraversal(node.left)
    result.append(node.data)
    if node.right:
        result += inOrderTraversal(node.right)
    return result


def postOrderTraversal(node):
    result = []
    if node.left:
        result += postOrderTraversal(node.left)
    if node.right:
        result += postOrderTraversal(node.right)
    result.append(node.data)
    return result


def bfsTraversal(node):
    if node is None:
        return
    result = []
    queue = Queue()
    queue.put(node)
    while not queue.is_empty():
        current_node = queue.get()
        result.append(current_node.data)
        if current_node.left:
            queue.put(current_node.left)
        if current_node.right:
            queue.put(current_node.right)
    return result


def pretty_print(node=None, level=0, prefix="Root: "):
    if node is None:
        return
    print("    " * level + prefix + str(node.data))
    if node.left:
        pretty_print(node.left, level + 1, prefix="L--- ")
    if node.right:
        pretty_print(node.right, level + 1, prefix="R--- ")


# ============= TESTE =============
root = None
letters = [8, 9, 10, 11, 12, 13]
for letter in letters:
    root = insert(root, letter)

print()
print("*="*20)

print('Altura da árvore:', getHeight(root))
print("In-order:", inOrderTraversal(root))
print("Pré-order:", preOrderTraversal(root))
print("Pós-order:", postOrderTraversal(root))
print("BFS:", bfsTraversal(root))
pretty_print(root)

root = insert(root, 10)

print("\nDeletando nó 9:")
root = delete(root, 9)
pretty_print(root)
