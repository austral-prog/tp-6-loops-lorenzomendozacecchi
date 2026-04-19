# Replace the "ANSWER HERE" for your answer

def enumerate_list(lst):
    """
    Dada una lista de strings, retorna una nueva lista donde cada elemento
    tiene el formato "indice. valor". Los strings vacios se deben saltear
    y no deben aparecer en la lista resultante.
    El indice debe ser consecutivo (no el indice original).

    Ejemplo: enumerate_list(["Red", "Green", "", "White"]) -> ["0. Red", "1. Green", "2. White"]
    """
    resultado = []
    indice = 0
    for i in range(len(lst)):
        if lst[i] != "":
            texto = str(indice) + ". " + lst[i]
            resultado.append(texto)
            indice = indice + 1
    return resultado


def enumerate_backwards(lst):
    """
    Igual que enumerate_list, pero cada palabra debe estar escrita al reves.
    Los strings vacios se deben saltear.

    Ejemplo: enumerate_backwards(["Red", "Green", ""]) -> ["0. deR", "1. neerG"]
    """
    resultado = []
    indice = 0
    for i in range(len(lst)):
        if lst[i] != "":
            backwards = lst[i][::-1]
            texto = str(indice) + ". " + backwards
            resultado.append(texto)
            indice = indice + 1
    return resultado  # Remove this line and implement
