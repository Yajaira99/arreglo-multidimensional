# Crear una matriz bidimensional (3x3)
matriz = [
    [3, 2, 1],
    [5, 4, 6],
    [9, 8, 7],
]

# Búsqueda de un valor específico en la matriz
valor_buscado = 8
valor_encontrado = False
fila_encontrada = -1
columna_encontrada = -1

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:
            valor_encontrado = True
            fila_encontrada = fila
            columna_encontrada = columna
            break  # Detener la búsqueda una vez que se encuentra el valor
    if valor_encontrado:
        break

# Mostrar el resultado de la búsqueda
if valor_encontrado:
    print(f"Se encontró {valor_buscado} en la posición ({fila_encontrada}, {columna_encontrada}) de la matriz.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")