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
    print('Rotacao direita em: ', y.data)
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    return x


def leftRotate(x):
    print('Rotacao esquerda em: ', x.data)
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


def pretty_print(node=None, prefix="", is_left=True):
    if node is not None:
        pretty_print(node.right, prefix + ("│   " if is_left else "    "), False)
        
        print(prefix + ("└── " if is_left else "┌── ") + str(node.data))

        pretty_print(node.left, prefix + ("    " if is_left else "│   "), True)


# ============= TESTE =============
root = None
while True:
    print("""
Escolha uma opção:
    1. Inserir nó(s)
    2. Deletar nó(s)
    3. Imprimir árvore
    4. Imprimir árvore em BFS
    5. Imprimir árvore em ordem
    6. Imprimir árvore em pré-ordem
    7. Imprimir árvore em pós-ordem
    8. Ver altura da árvore
    9. Ver fator de balanceamento da raiz
    10. Sair
    """, end="")

    choice = input("Opção: ")
    print()

    if choice == "1":
        while True:
            try:
                num = int(input("Digite o valor a ser inserido: (letra para encerrar):  "))
                root = insert(root, num)
            except ValueError:
                break
    elif choice == "2":
        while True:
            try:
                num = int(input("Digite o valor a ser deletado: (letra para encerrar):  "))
                root = delete(root, num)
            except ValueError:
                break
    elif choice == "3":
        pretty_print(root)
    elif choice == "4":
        print("BFS:", bfsTraversal(root))
    elif choice == "5":
        print("In-order:", inOrderTraversal(root))
    elif choice == "6":
        print("Pré-order:", preOrderTraversal(root))
    elif choice == "7":
        print("Pós-order:", postOrderTraversal(root))
    elif choice == "8":
        print('Altura da árvore:', getHeight(root))
    elif choice == "9":
        print('Fator de balanceamento da raiz:', getBalance(root))
    elif choice == "10":
        break
    else:
        print("Opção inválida.")
