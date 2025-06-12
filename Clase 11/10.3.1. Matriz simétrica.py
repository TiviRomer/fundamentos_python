'''
Clase:        Clase 11
Tema:         Manejo de matrices
Ejercicio:    10.3.1. Matriz simétrica
Descripción:  Dada una matriz cuadrada ingresada por el usuario, comprueba si la matriz cuadrada es
              simétrica respecto a su diagonal principal.
              Entrada:
                • Numero entero N con la dimensión de la matriz. N conjuntos de números enteros separados por coma.
              Salida:
                • Una línea con una cadena de texto. “La matriz es simétrica” si es simétrica; “La matriz no es simétrica” en caso contrario.
Autor:        Steven Josué Romero Salmerón
Fecha:        2025-06-12
Estado:       [ Terminado ]
'''
n = int(input())

#Se crea la matriz y se guarda cada fila utilizando un for con el numero n de filas a ingresar
matriz = [list(map(int, input().split(','))) for i in range(n)]

simetrica = True

for i in range(n):
    for j in range(n):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break

if simetrica == True:
    print("\nLa matriz es simétrica")
else:
    print("\nLa matriz no es simétrica")