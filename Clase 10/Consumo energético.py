import numpy as np

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

#Exploración inicial de datos
print("Dimensiones:", consumo.ndim)                       #2 (Filas y columnas)
print("Forma:", consumo.shape)                            #(10, 7) 10 filas y 7 columnas
print("Tipo de datos:", consumo.dtype)                    #float64 (números decimales)
print("Consumo primer hogar:", consumo[0])                #Todos los datos de la fila 0
print("Consumo el miércoles (día 3):", consumo[:, 2])     #Todos los datos de la columna 2

# Promedio de consumo por hogar
promedio_por_hogar = np.mean(consumo, axis = 1)

# Promedio de consumo diario de todos los hogares
promedio_por_dia = np.mean(consumo, axis = 0)

# Suma total de consumo en la semana de los 10 hogares
total_consumo = np.sum(consumo)

print()
print(promedio_por_hogar)
print(promedio_por_dia)
print(total_consumo)

# Máximo por hogar
maximos = np.max(consumo, axis = 1)

# Mínimo por día
minimos = np.min(consumo, axis = 0)

# Desviación estándar global
desviacion = np.std(consumo)

print()
print(maximos)
print(minimos)
print(desviacion)

# suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis = 1)
# Índice del hogar con mayor consumo
hogar_mayor_consumo = np.argmax(consumo_total_hogar)
# Índice del hogar con mejor consumo
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

print()
print(consumo_total_hogar)
print(hogar_mayor_consumo)
print(hogar_mas_eficiente)
      
# Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis = 1)
print()
print(f"Consumo total de cada hogar durante la semana: {consumo_total_hogar}")

# Compara cada hogar con un valor mayor a 100
altos = consumo_total_hogar > 100
# Filtrando hogares que cumplen la condición:
consumo_mayor_100 = np.where(altos)[0]

print(f"ids de hogare con consumo mayor a 100: {consumo_mayor_100}")

# Aplicando normalización MinMax al conjunto de datos
consumo_normalizado = (consumo - consumo.min() / (consumo.max()  - consumo.min()))

# Resultado
print()
print(consumo_normalizado)

# Sección de preguntas

# 1. ¿Cuál es el consumo del hogar 5 el vienes (día 5)?
print()
print(f"El consumo energetico del hogar 5 el día viernes es de: {consumo[4, 4]} kW/h")

# 2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
print()
print(f"El consumo energetico de los tres ultimos hogares el domingo es de: {consumo[-3:, 0]} kW/h")

# 3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
promedio_fines_semana = (np.sum(consumo[:, 0]) + np.sum(consumo[:, 6])) / 20

print()
print(f"El promedio de consumo de los fines de semana es de: {promedio_fines_semana} kW/h")

# ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
desviacion_dia = np.std(consumo, axis = 0)

print()
print(f"El dia de la semana con mayor desviacion estandar es el día {np.argmax(desviacion_dia)}")
# El dia de la semana con mayor desviación estandar es el viernes (día 5) porque sacamos el indice con el valor mas alto de la lista de desviación estandar de cada día.
# Esto quiere decir que el dia viernes (día 5) es donde los hogares tienen los consumos mas variados.

# Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
hogares_menor_consumo = np.argsort(consumo_total_hogar)[:3]

print()
print(f"Los 3 hogares con menor consumo total son: {hogares_menor_consumo}")
print(f"Los valores de consumo de esos 3 hogares son: {consumo_total_hogar[hogares_menor_consumo]}")

# 6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
hogar3_aumento = np.sum((consumo[2, :] + (consumo[2, :] * 10) / 100))

print()
print(f"Si el hogar 3 aumenta su consumo en un 10% cada dia, su nuevo consumo total semanal es de: {hogar3_aumento}")