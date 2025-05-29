'''
Clase:        Clase 5
Tema:         Bloque condicional
Ejercicio:    5.4.2. Sumador de valores posicionales
Descripción:  Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito.
              Ejemplo:
                Si el usuario ingresa 9875, entonces: 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2.
                Entrada:
                  • Un numero entero.
                Restricciones:
                  • 1 ≤ número ≤ 10^9
                Conceptos explorados:
                  • Bucles y control de flujo.
Autor:        Steven Josué Romero Salmerón
Fecha:        2025-05-28
Estado:       [ Terminado ]
'''

num = int(input("Ingresa un número: "))

num = str(num)

print(f"\nProceso de reducción para {num}: ")
while len(num) != 1:
   num2 = 0 

   for i in num:
      num2 += int(i)

   print(f"{num} = {num2}")

   num = str(num2)

print(f"\nEl resultado final es: {num}")