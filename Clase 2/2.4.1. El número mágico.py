'''
Clase:        Clase 2
Tema:         Bloque condicional
Ejercicio:    2.4.1. El número mágico
Descripción:  Crea un programa en Python para determinar si un número es "mágico“.
              Un número es “mágico” si es divisible por 7 pero no por 5.
              Entrada:
                • Un entero n
              Salida:
                • "Mágico" o "Normal"
              Restricciones:
                • 1 ≤ n ≤ 10^18
Autor:        Steven Josué Romero Salmerón
Fecha:        2025-05-21
Estado:       [ Terminado ]
'''
def numeroMagico(num):
    if(num % 7 == 0  and num % 5 != 0):
        return print("Magico")
    else:
        return print("No magico")
    
num = int(input("Ingrese un numero: "))
numeroMagico(num)