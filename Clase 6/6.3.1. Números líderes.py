'''
Clase:        Clase 6
Tema:         Manejo de listas
Ejercicio:    6.3.1. Números líderes
Descripción:  Un número en una lista es "líder" si es estrictamente mayor que todos los elementos a su derecha. 
              Dada una lista de números ingresada por el usuario, imprime todos los números líderes.
              Entrada:
                • La primera línea contiene n enteros a₁, ..., aₙ(1 ≤ aᵢ ≤ 10⁹)
              Salida:
                • Una línea con todos los números líderes en el orden en que aparecen en el arreglo.
Autor:        Steven Josué Romero Salmerón
Fecha:        2025-05-28
Estado:       [ Terminado ]
'''

def encuentra_lideres(lista):
    lideres = []
    max_derecha = float('-inf')
    for num in reversed(lista):
        if num > max_derecha:
            lideres.append(num)
            max_derecha = num
    return lideres[::-1]

lista = list(map(int, input().split()))

lideres = encuentra_lideres(lista)

print(*lideres)