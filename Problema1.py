# Inicializar variables
suma_positivos = 0
suma_negativos = 0
contador_positivos = 0
contador_negativos = 0


for i in range(20):
    numero = float(input("Ingrese un número: "))
    if numero >= 0:
        suma_positivos += numero
        contador_positivos += 1
    else:
        suma_negativos += numero
        contador_negativos += 1


promedio_positivos = suma_positivos / contador_positivos
promedio_negativos = suma_negativos / contador_negativos


print(f"El promedio de los números positivos es: {promedio_positivos}")
print(f"El promedio de los números negativos es: {promedio_negativos}")
