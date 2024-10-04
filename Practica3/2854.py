class UnionFind:
    def __init__(self, tamano):
        # Inicializamos cada persona como su propio representante (padre) y el rango
        self.padre = list(range(tamano))
        self.rango = [1] * tamano

    def encontrar(self, p):
        # Metodo para encontrar la raiz de una persona con compresion de caminos
        if self.padre[p] != p:
            self.padre[p] = self.encontrar(self.padre[p])
        return self.padre[p]

    def unir(self, p, q):
        # Unimos dos personas si pertenecen a familias diferentes
        raizP = self.encontrar(p)
        raizQ = self.encontrar(q)
        
        if raizP != raizQ:
            # Unimos segun el rango (altura de los arboles)
            if self.rango[raizP] > self.rango[raizQ]:
                self.padre[raizQ] = raizP
            elif self.rango[raizP] < self.rango[raizQ]:
                self.padre[raizP] = raizQ
            else:
                self.padre[raizQ] = raizP
                self.rango[raizP] += 1

def resolver():
    # Leemos el numero de personas y relaciones
    M, N = map(int, input().split())
    personas = {}
    contador_personas = 0

    # Creamos una instancia de UnionFind para manejar M personas
    uf = UnionFind(M)

    # Funcion auxiliar para asignar un identificador unico a cada persona
    def obtener_id_persona(nombre):
        nonlocal contador_personas
        if nombre not in personas:
            personas[nombre] = contador_personas
            contador_personas += 1
        return personas[nombre]

    # Leemos y procesamos las relaciones
    for _ in range(N):
        persona1, relacion, persona2 = input().split()
        id1 = obtener_id_persona(persona1)
        id2 = obtener_id_persona(persona2)
        uf.unir(id1, id2)

    # Contamos cuantas familias diferentes existen
    familias_distintas = set()
    for i in range(contador_personas):
        familias_distintas.add(uf.encontrar(i))

    # Mostramos el numero de familias distintas
    print(len(familias_distintas))

resolver()