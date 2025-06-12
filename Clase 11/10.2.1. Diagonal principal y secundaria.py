'''
Clase:        Clase 11
Tema:         Manejo de matrices
Ejercicio:    10.2.1. Diagonal principal y secundaria
Descripción:  Dada una matriz cuadrada ingresada por el usuario, crea dos listas, una con los
              elementos de la diagonal principal y la otra con los elementos de la diagonal secundaria.
              Entrada:
                • Numero entero N con la dimensión de la matriz. N conjuntos de números enteros separados por coma.
              Salida:
                • Dos listas, una con los elementos de la diagonal principal y la otra con los elementos de la diagonal secundaria.
Autor:        Steven Josué Romero Salmerón
Fecha:        2025-06-12
Estado:       [ Terminado ]
'''

n = int(input())

#Se crea la matriz y se guarda cada fila utilizando un for con el numero n de filas a ingresar
matriz = [list(map(int, input().split(','))) for i in range(n)]

dPrincipal = [matriz[i][i] for i in range(n)]
dSecundaria = [matriz[i][n - 1 - i] for i in range(n)]

print()
print(dPrincipal)
print(dSecundaria)