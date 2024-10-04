def invertir_mitad_y_combinar(s):
    indice_mitad = len(s) // 2
    primera_mitad_invertida = s[:indice_mitad][::-1]
    segunda_mitad_invertida = s[indice_mitad:][::-1]
    resultado = primera_mitad_invertida + segunda_mitad_invertida
    return resultado

def principal():
    import sys
    entrada = sys.stdin.read
    datos = entrada().splitlines()
    num_casos = int(datos[0])
    
    resultados = []
    for i in range(1, num_casos + 1):
        resultados.append(invertir_mitad_y_combinar(datos[i]))
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    principal()
