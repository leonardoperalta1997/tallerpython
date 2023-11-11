
salario_total = 0
n = int(input("Ingrese la cantidad de lavadores: "))


for i in range(n):
    
    sedanes = int(input(f"Lavador {i + 1} - Sedanes: "))
    grandes = int(input(f"Lavador {i + 1} - Autos grandes: "))

    
    salario = (sedanes * 2.50) + (grandes * 4.00)

    
    salario_total += salario

    
    print(f"Lavador {i + 1} - Total a pagar: ${salario:.2f}")


print(f"Salario total a pagar: ${salario_total:.2f}")