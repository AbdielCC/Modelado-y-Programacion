cjto_pokemones_obtenidos = set()
numero = int(input())

for _ in range(numero):
    pokemon = input().strip()
    cjto_pokemones_obtenidos.add(pokemon)

total_pokemones = 151
faltan = total_pokemones - len(cjto_pokemones_obtenidos)
print(f"Falta(m) {faltan} pomekon(s).")
