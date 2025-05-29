'''
Clase:        Clase 2
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
Fecha:        2025-05-21
Estado:       [ Terminado ]
'''

def contraseña (contra):
    mayus = False
    num = False

    if len(contra) < 8:
        return print("Contraseña no segura")
    
    for i in contra:
        if i.isupper():
            mayus = True
        if i.isdigit():
            num = True

    if mayus and num:
        return print("Contraseña segura")
    else:
        return print("Contraseña no segura")
    

contra = input("Ingrese una contraseña: ")
contraseña(contra)