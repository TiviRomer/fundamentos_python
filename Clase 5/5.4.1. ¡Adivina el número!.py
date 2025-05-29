'''
Clase:        Clase 5
Tema:         Bloque condicional
Ejercicio:    5.4.1. ¡Adivina el número!
Descripción:  Genera un número aleatorio entre 1 y 100 y pide al usuario que lo adivine.
              El programa debe seguir pidiendo números hasta que acierte. En cada intento fallido el programa 
              notificará al usuario si el número secreto es mayor o menor al último valor ingresado.
              Entrada:
                • Números enteros entre 1 y 100.
              Salida:
                • Tres posibles salidas: “El número secreto es menor”, “El número secreto es mayor”, 
                  ¡Felicidades! Has adivinado el número secreto”
Autor:        Steven Josué Romero Salmerón
Fecha:        2025-05-28
Estado:       [ Terminado ]
'''
import random

numR = random.randint(1, 100)
acierto = False
num = 0

while not acierto:
  num = int(input("Ingrese un numero 1 y 100: "))

  if num == numR:
    print(f"¡Felicidades! Has adivinado el numero secreto: {numR}")
    acierto = True
  elif num > numR:
    print("El numero secreto es menor")
  else:
    print("El numero secreto es mayor")

print("Fin del juego")