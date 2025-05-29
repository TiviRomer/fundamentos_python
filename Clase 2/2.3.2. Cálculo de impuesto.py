'''
Clase:        Clase 2
Tema:         Bloque condicional
Ejercicio:    2.3.2. Cálculo de impuesto
Descripción:  Desarrollar un programa en Python que permita calcular el impuesto que debe pagar
              un usuario por el consumo de energía. El cálculo debe realizarse basado en la siguiente tabla.
               Unidades consumidas          Nombre
                     0 - 100             Sin impuestos
                    101 - 200         $0.5 por cada unidad
                    201 o más         $0.7 por cada unidad
              Entrada:
                • Unidades consumidas (entero).
              Salida:
                • Impuesto aplicado ($).
              Restricciones:
                • Sin restricciones.
Autor:        Steven Josué Romero Salmerón
Fecha:        2025-05-21
Estado:       [ Terminado ]
'''

def impuesto(unidad):
    imp = 0.0
    if(unidad > 100 and unidad <= 200):
        imp = unidad * 0.5
    elif(unidad > 200):
        imp = unidad * 0.7
    
    return print(f"Impuesto aplicado: ${round(imp, 2)}")

unidad = int(input("Ingrese la cantidad de unidades: "))
impuesto(unidad)