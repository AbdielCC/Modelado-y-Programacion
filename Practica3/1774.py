class conjdis:
    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0] * n

    def encontrar(self, u):
        if self.padre[u] != u:
            self.padre[u] = self.encontrar(self.padre[u])
        return self.padre[u]

    def unir(self, u, v):
        raiz_u = self.encontrar(u)
        raiz_v = self.encontrar(v)
        if raiz_u != raiz_v:
            if self.rango[raiz_u] > self.rango[raiz_v]:
                self.padre[raiz_v] = raiz_u
            elif self.rango[raiz_u] < self.rango[raiz_v]:
                self.padre[raiz_u] = raiz_v
            else:
                self.padre[raiz_v] = raiz_u
                self.rango[raiz_u] += 1

def kruskal(n, aristas):
    aristas.sort(key=lambda x: x[2])
    cd = conjdis(n)
    costo_total = 0
    num_aristas = 0

    for u, v, costo in aristas:
        if cd.encontrar(u) != cd.encontrar(v):
            cd.unir(u, v)
            costo_total += costo
            num_aristas += 1
            if num_aristas == n - 1:
                break

    return costo_total

R, C = map(int, input().split())
aristas = []

for _ in range(C):
    V, W, P = map(int, input().split())
    aristas.append((V - 1, W - 1, P))

print(kruskal(R, aristas))
