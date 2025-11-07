#Calculadora Basica

print("---Calculadora basica---")
print("1.Suma")
print("2.Resta")
print("3.Multiplicacion")
print("4.División")


opcion = input("Selecciona 1 de las 4 opciones: 1-2-3-4:  ")

numero1 = float(input("Ingresa el primer digito para ser operado: "))
numero2 = float(input("Ingresa el segundo digito para ser operado: "))

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

print(f"El resultado de la {operacion} es: {resultado}")    