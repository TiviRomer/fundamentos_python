'''
Clase:        Clase 11
Tema:         Manejo de matrices
Ejercicio:    10.3.2. Juego del entorno
Descripción:  Dada una matriz binaria ingresada por el usuario, verifica para cada celda de una
              matriz binaria cuántos elementos con valor de 1 hay en las celdas vecinas (arriba, abajo, izquierda, derecha, diagonales).
              Entrada:
                • Dos números N,M con la dimensión de la matriz. N conjuntos de M cantidad de números enteros separados por coma.
              Salida:
                • Matriz NxM. Cada celda contiene la suma de elementos con valor de 1 en las celdas vecinas.
Autor:        Steven Josué Romero Salmerón
Fecha:        2025-06-12
Estado:       [ En progreso ]
'''

n = int(input())
m = int(input())
matriz = []

for i in range(n):
    matriz.append(list(map(int, input().split(','))))

for i in range(n):
    for j in range(m):
        print(matriz[i][j], end=" ")
    print()