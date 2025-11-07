# Generador de Propinas

Cuenta = float(input("Digite su cuenta antes de la propina: "))

malo = Cuenta * 0.05
regular = Cuenta * 0.10
bueno = Cuenta * 0.15
excelente = Cuenta * 0.20

def opcion1():
    print("Opción seleccionada: malo → 5% de propina")

def opcion2():
    print("Opción seleccionada: regular → 10% de propina")

def opcion3():
    print("Opción seleccionada: bueno → 15% de propina")

def opcion4():
    print("Opción seleccionada: excelente → 20% de propina")

def opcion5():
    print("Ha salido del menú. Gracias por usar el generador de propinas.")
    exit()  # Termina el programa

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Malo")
    print("2. Regular")
    print("3. Bueno")
    print("4. Excelente")
    print("5. Salir")
    print("------------------------")

while True:
    mostrar_menu()
    opcion = input("Ingresa tu opción: ")

    if opcion == '1':
        opcion1()
        print(f"Propina: ${malo:.2f}")
        print(f"Total a pagar: ${Cuenta + malo:.2f}")

    elif opcion == '2':
        opcion2()
        print(f"Propina: ${regular:.2f}")
        print(f"Total a pagar: ${Cuenta + regular:.2f}")

    elif opcion == '3':
        opcion3()
        print(f"Propina: ${bueno:.2f}")
        print(f"Total a pagar: ${Cuenta + bueno:.2f}")

    elif opcion == '4':
        opcion4()
        print(f"Propina: ${excelente:.2f}")
        print(f"Total a pagar: ${Cuenta + excelente:.2f}")

    elif opcion == '5':
        opcion5()

    else:
        print("Opción inválida. Por favor, intenta de nuevo.")