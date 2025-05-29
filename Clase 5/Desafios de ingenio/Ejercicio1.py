'''
Clase:        Clase 3
Tema:         Bloque condicional
Ejercicio:    2.3.1. Contraseña segura
Descripción:  Solicita una cadena de texto que representa una contraseña, y verifica si la contraseña
              cumple con las siguientes condiciones: tener al menos 8 caracteres, un número y una mayúscula.
              Entrada:
                • Una cadena de texto
              Salida:
                • Dos posibles valores: "Contraseña segura" o "Contraseña no segura".
              Restricciones:
                • Sin restricciones
              Sugerencia:
                • Investigar sobre los métodos isdigit() y isupper()
Autor:        Steven Josué Romero Salmerón
Fecha:        2025-05-28
Estado:       [ Terminado ]
'''

def rombo():
    for i in range(1, 4):
        print(" " * (3 - i) + "*" * (2 * i - 1))
    for i in range(2, 0, -1):
        print(" " * (3 - i) + "*" * (2 * i - 1))

def figura2():
    for i in range(1, 6):
        if i % 2 != 0:
            for j in range(1, 6):
                if j % 2 != 0:
                    print("_", end="")
                else:
                    print("-", end="")
        else:
            for j in range(1, 6):
                if j % 2 != 0:
                    print("-", end="")
                else:
                    print("_", end="")
        print()

for i in range(0, 2):
    print(f"{rombo()}", end="")
    print(f"{figura2()}", end="")