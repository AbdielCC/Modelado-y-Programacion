class Nodo:
    def __init__(self, valor):
        self.izq = None
        self.der = None
        self.valor = valor

class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar(valor, nodo.izq)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar(valor, nodo.der)

    def preorden(self, nodo, resultado):
        if nodo:
            resultado.append(str(nodo.valor))
            self.preorden(nodo.izq, resultado)
            self.preorden(nodo.der, resultado)

    def inorden(self, nodo, resultado):
        if nodo:
            self.inorden(nodo.izq, resultado)
            resultado.append(str(nodo.valor))
            self.inorden(nodo.der, resultado)

    def postorden(self, nodo, resultado):
        if nodo:
            self.postorden(nodo.izq, resultado)
            self.postorden(nodo.der, resultado)
            resultado.append(str(nodo.valor))

C = int(input())
for caso in range(1, C + 1):
    N = int(input())
    numeros = list(map(int, input().split()))
    
    bst = BST()
    for numero in numeros:
        bst.insertar(numero)
    
    pre = []
    ino = []
    post = []
    
    bst.preorden(bst.raiz, pre)
    bst.inorden(bst.raiz, ino)
    bst.postorden(bst.raiz, post)
    
    print(f"Case {caso}:")
    print("Pre.: " + " ".join(pre))
    print("In..: " + " ".join(ino))
    print("Post: " + " ".join(post))
    print()
