class ClienteBanco:
    def __init__(self, nombre: str, edad: int, ciudad: str, estrato: int, ingresos: float):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
        self.estrato = estrato
        self.ingresos = ingresos

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Ciudad: {self.ciudad}")
        print(f"Estrato: {self.estrato}")
        print(f"Ingresos: ${self.ingresos:,.2f}")
        print("-" * 40)

class BaseDatosClientesBanco:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente: ClienteBanco):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nombre} agregado exitosamente.")

    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes en la base de datos.")
            return
        print("Listado de clientes:")
        for c in self.clientes:
            c.mostrar_datos()

    def buscar_por_ciudad(self, ciudad: str):
        resultados = [c for c in self.clientes if c.ciudad.lower() == ciudad.lower()]
        if not resultados:
            print(f"No se encontraron clientes en la ciudad {ciudad}.")
        else:
            print(f"Clientes en la ciudad {ciudad}:")
            for c in resultados:
                c.mostrar_datos()

    def resumen_ingresos_por_estrato(self):
        resumen = {}
        for c in self.clientes:
            resumen.setdefault(c.estrato, []).append(c.ingresos)

        print("Resumen de ingresos por estrato:")
        for estrato, ingresos in resumen.items():
            promedio = sum(ingresos) / len(ingresos)
            print(f"Estrato {estrato}: {len(ingresos)} clientes, ingreso promedio ${promedio:,.2f}")

# Ejemplo de uso

bd = BaseDatosClientesBanco()

c1 = ClienteBanco("Andres Alonso", 28, "Bogotá", 3, 2500000)
c2 = ClienteBanco("Maria Perez", 35, "Medellín", 4, 3000000)
c3 = ClienteBanco("Juan Gomez", 40, "Bogotá", 2, 1800000)

bd.agregar_cliente(c1)
bd.agregar_cliente(c2)
bd.agregar_cliente(c3)

bd.listar_clientes()
bd.buscar_por_ciudad("Bogotá")
bd.resumen_ingresos_por_estrato()
