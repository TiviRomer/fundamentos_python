'''
Clase:        Clase 1
Tema:         Variables, tios, entradas y salidas
Ejercicio:    1.4.1. División con Precisión
Descripción:  Dados tres enteros a, b y k, imprime el resultado de a / b con k decimales exactos (sin redondear).
              Entrada:
                • a y b (-10⁹ ≤ a, b ≤ 10⁹), k (1 ≤ k ≤ 1000).
              Salida:
                • Una cadena con la división exacta, incluyendo k decimales (truncados).
              Restricciones:
                • No es posible dar formato utilizando "{:.{k}f}“ para redondear los decimales.
Autor:        Steven Josué Romero Salmerón
Fecha:        2025-05-21
Estado:       [ Terminado ]
'''

def cortarDecimales(numero, decimales):
    cString = str(numero)
    nNum = ""
    index = 0

    for i in cString:
        nNum += i

        if i == ".":
            dString = cString[index+1::]

            for c in range(decimales):
                try:
                    nNum += dString[c]
                except:
                    nNum += "0"
            break

        index += 1

    return print(nNum)

a =  float(input("Ingrese un numero: "))
b =  float(input("Ingrese otro numero: "))
d = int(input("Ingrese la cantidad de decimales: "))

c =  float( a / b)

cortarDecimales(c, d)