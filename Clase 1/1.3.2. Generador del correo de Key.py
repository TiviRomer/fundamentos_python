'''
Clase:        Clase 1
Tema:         Variables, tios, entradas y salidas
Ejercicio:    1.3.2. Generador del correo de Key
Descripción:  Solicita al usuario su nombre completo (asume dos nombres y dos apellidos). 
              Luego, el programa generará, su correo con el formato:
              • primer_nombre.primer_apellido@keyinstitute.edu.sv

Autor:        Steven Josué Romero Salmerón
Fecha:        2025-05-21
Estado:       [ Terminado ]
'''

def correoKey(primerN, primerA):
    return f"{primerN.lower()}.{primerA.lower()}@keyinstitute.edu.sv"

primerN = input("Ingrese su primer nombre: ")
segundoN = input("Ingrese su segundo nombre: ")
primerA = input("Ingrese su primer apellido: ")
segundoA = input("Ingrese su segundo apellido: ")

email = correoKey(primerN, primerA)

print(email)