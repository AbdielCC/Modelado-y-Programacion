def decodificar_cifrado_cesar(mensaje, valor_desplazamiento):
    caracteres_decodificados = [
        chr((ord(char) - valor_desplazamiento - 65) % 26 + 65) for char in mensaje
    ]
    return ''.join(caracteres_decodificados)

def main():
    import sys
    input_data = sys.stdin.read().splitlines()
    
    case_count = int(input_data[0])
    decoded_results = []
    
    for i in range(case_count):
        msg = input_data[2 * i + 1]
        shift = int(input_data[2 * i + 2])
        decoded_results.append(decodificar_cifrado_cesar(msg, shift))
    
    for result in decoded_results:
        print(result)

if __name__ == "__main__":
    main()
