# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    lista = []
    for indice in range(len(matrix)): #recorre los indices de cada sublista
        for j in matrix[indice]:
            lista.append(j)
    return lista

def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    lista = []
    for indice in range(len(matrix)):
        suma = 0
        for j in matrix[indice]:
            suma = j + suma
        lista.append(suma)
    return lista  # Remove this line and implement


def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    lista = []
    for columna in range(len(matrix[0])):
        suma = 0
        for fila in range(len(matrix)):
             suma = suma + matrix[fila][columna]
        lista.append(suma)
    return lista  # Remove this line and implement
