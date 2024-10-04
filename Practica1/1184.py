op = input().strip()

matriz = []
for i in range(12):
    fila = []
    for j in range(12):
        valor = float(input().strip())
        fila.append(valor)
    matriz.append(fila)


total = 0
cuenta = 0

for i in range(1, 12):  
    for j in range(0, i):
        total += matriz[i][j]
        cuenta += 1

if op == 'S':
    resultado = total
elif op == 'M':
    resultado = total / cuenta

print(f"{resultado:.1f}")

