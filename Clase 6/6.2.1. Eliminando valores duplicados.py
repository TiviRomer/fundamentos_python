'''
Clase:        Clase 6
Tema:         Manejo de listas
Ejercicio:    6.2.1. Eliminando valores duplicados
Descripción:  Dada una lista ingresada por el usuario, elimina los elementos duplicados manteniendo la primera aparición 
              de cada número.
              Entrada:
                • La primera línea contiene n enteros a₁, ..., aₙ (1 ≤ aᵢ ≤ 10⁶)
              Salida:
                • Una línea con los enteros únicos en su orden de aparición, separados por espacios.
Autor:        Steven Josué Romero Salmerón
Fecha:        2025-05-28
Estado:       [ Terminado ]
'''
lista = list(map(int, input().split()))

listaU = dict.fromkeys(lista)

print()

print(*listaU)