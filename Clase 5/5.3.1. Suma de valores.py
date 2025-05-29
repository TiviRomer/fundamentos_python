'''
Clase:        Clase 5
Tema:         Bloque condicional
Ejercicio:    5.3.1. Suma de valores
Descripción:  Dada una lista de longitud variable de números enteros ingresada por el usuario,
              calcula e imprime la suma de todos los números usando un bucle for.
              Entrada:
                • Una lista de longitud variable ingresada por el usuario.
              Salida:
                • Suma de todos los componentes de la lista.
              Restricciones:
                • Sin restricciones
Autor:        Steven Josué Romero Salmerón
Fecha:        2025-05-28
Estado:       [ Terminado ]
'''

def suma(lista):
    sum = 0

    for i in lista:
        sum += i

    return sum    

lista = []
cant = int(input("cuantos numeros va a agregar?: "))
print()

for i in range(cant):
    lista.append(int(input("Ingrese el numero: ")))

suma = suma(lista)

print(f"\nLa suma de los numeros es: {suma}")