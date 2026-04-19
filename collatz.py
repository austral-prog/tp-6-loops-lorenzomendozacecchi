# Replace the "ANSWER HERE" for your answer

def collatz_steps(n):
    """
    Retorna la cantidad de pasos necesarios para llegar a 1
    siguiendo la conjetura de Collatz:
      - Si n es par: n = n // 2
      - Si n es impar: n = 3 * n + 1

    n debe ser >= 1. Si n es 1, retorna 0 (ya esta en 1).

    Ejemplo: collatz_steps(6) -> 8
      6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1  (8 pasos)
    """
    contador = 0
    if n == 1:
        return 0
    else:

        while n != 1:
            if n % 2 == 0:
               n = n // 2
               contador = contador + 1
            elif n % 2 != 0:
                 n = 3 * n + 1
                 contador = contador + 1
    return contador


def collatz_sequence(n):
    """
    Retorna la secuencia completa de Collatz como una lista,
    comenzando desde n y terminando en 1.

    n debe ser >= 1. Si n es 1, retorna [1].

    Ejemplo: collatz_sequence(6) -> [6, 3, 10, 5, 16, 8, 4, 2, 1]
    """
    if n == 1:
        lista = [n]
        return lista
    else:
        lista = [n]
        while n != 1 and n != 0:
            if n % 2 == 0:
                n = n//2
                lista.append(n)
            elif n % 2 != 0:
                n = 3 * n + 1
                lista.append(n)
    return lista  # Remove this line and implement
