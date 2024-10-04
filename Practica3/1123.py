import heapq

def dijkstra(grafo, distancias, C, K, N):
    cola = []
    heapq.heappush(cola, (0, K))
    distancias[K] = 0

    while cola:
        distancia_actual, ciudad_actual = heapq.heappop(cola)

        if distancia_actual > distancias[ciudad_actual]:
            continue

        for vecino, costo in grafo[ciudad_actual]:
            nueva_distancia = distancia_actual + costo

            if ciudad_actual < C and vecino == ciudad_actual + 1:
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    heapq.heappush(cola, (nueva_distancia, vecino))
            elif ciudad_actual >= C or vecino >= C:
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    heapq.heappush(cola, (nueva_distancia, vecino))

def resolver():
    while True:
        N, M, C, K = map(int, input().split())
        if N == 0 and M == 0 and C == 0 and K == 0:
            break

        grafo = [[] for _ in range(N)]
        for _ in range(M):
            U, V, P = map(int, input().split())
            grafo[U].append((V, P))
            grafo[V].append((U, P))

        distancias = [float('inf')] * N

        dijkstra(grafo, distancias, C, K, N)

        print(distancias[C-1])

resolver()
