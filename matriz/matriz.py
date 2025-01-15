def validar_matriz(matriz):
    # Verificar filas
    for fila in matriz:
        if sum(fila) != 45: 
            return False

    # Verificar columnas
    for col in range(9):
        if sum(matriz[fila][col] for fila in range(9)) != 45:
            return False


    return True

matriz_ejemplo = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
]

if validar_matriz(matriz_ejemplo):
    print("La solucion es correcta")
else:
    print("La solucion es incorrecta")
