# Vamos a definir la clase dentro de Python para hacer una estructura sobre zapatos.

class Zapato_Puma_B1:
    def __init__(self):
        self.marca = "La marca de este calzado es Puma"
        self.talla = "la talla  que hay en Stock es 40"
        self.color = "El color de este calzado es azul menta "
        self.precio = "El precio de este calzado en stock es de 300 mil pesos colombianos"
        self.material = "El material es Cuero y caucho"
        self.tipo = "El tipo de este calzado es Deportivo"


# Crear instancia de la clase
zapato = Zapato_Puma_B1()

# Mostrar los atributos en pantalla
print(zapato.marca)
print(zapato.talla)
print(zapato.color)
print(zapato.precio)
print(zapato.material)
print(zapato.tipo)

