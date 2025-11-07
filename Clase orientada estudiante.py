#Definir los atributos de la clase Estudiante
class Estudiante:
    def __init__(self):
        # Se definen los atributos del conjunto
        self.nombre = "Alejandro Rodriguez"
        self.edad = "15 años"
        self.grado = "Noveno"
        self.estrato = "3"
        self.nacionalidad = "Colombiano"

# Crear una instancia de la clase Estudiante
persona = Estudiante()

# Imprimir los atributos del objeto
print(persona.nombre)
print(persona.edad)
print(persona.grado)
print(persona.estrato)
print(persona.nacionalidad)