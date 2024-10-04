def calcular_hash(cadenas):
    hash_total = 0
    for indice_cadena, cadena in enumerate(cadenas):
        hash_cadena = 0
        for posicion, caracter in enumerate(cadena):
            valor_letra = ord(caracter) - ord('A')
            hash_cadena += valor_letra + posicion + indice_cadena
        hash_total += hash_cadena
    return hash_total

def principal():
    import sys
    entrada = sys.stdin.read
    datos = entrada().splitlines()
    
    num_casos = int(datos[0])
    resultados = []
    indice_linea = 1
    
    for _ in range(num_casos):
        num_cadenas = int(datos[indice_linea])
        cadenas = datos[indice_linea + 1: indice_linea + 1 + num_cadenas]
        resultados.append(calcular_hash(cadenas))
        indice_linea += 1 + num_cadenas
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    principal()