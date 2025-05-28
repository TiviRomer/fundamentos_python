'''
Clase:        Clase 1
Tema:         Variables, tios, entradas y salidas
Ejercicio:    1.3.1. Automatizando el cálculo de la propina
Descripción:  Pide al usuario el total de una cuenta y el porcentaje de propina
              (por ejemplo, 10%, 15%, 20%). Calcula y muestra en pantalla el total
              a pagar.

Autor:        Steven Josué Romero Salmerón
Fecha:        2025-05-21
Estado:       [ Terminado ]
'''

def propina(total, porcentaje):
    return total * (porcentaje / 100)

totalOriginal = float(input("Ingrese el total de la cuenta: "))
porcentaje = float(input("Ingrese el porcentaje de propina: "))

totalPropina = propina(totalOriginal, porcentaje)

total = totalOriginal + totalPropina

print(f"Total de la cuenta: ${totalOriginal} \nPropina: ${totalPropina} \nTotal de la cuenta con propina ({porcentaje}%): ${total}")