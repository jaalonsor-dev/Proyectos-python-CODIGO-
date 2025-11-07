print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")


# Pedir al usuario que elija una operación
opcion = input("Elige una operación (1/2/3/4): ")

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
 Realizar la operación seleccionada
if opcion == "1":
    resultado = numero1 + numero2
    operacion = "suma"
elif opcion == "2":
    resultado = numero1 - numero2
    operacion = "resta"
elif opcion == "3":
    resultado = numero1 * numero2
    operacion = "multiplicación"
elif opcion == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
        operacion = "división"
    else:
        resultado = "Error: No se puede dividir por cero"
        operacion = "división"
else:
    resultado = "Opción inválida"
    operacion = "ninguna"

# Mostrar resultado
print(f"El resultado de la {operacion} es: {resultado}")
