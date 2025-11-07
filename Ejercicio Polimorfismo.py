class AnimalCarnivoro:
    def carnivoro(self):
        print("Este animal come carne")

# Clases hijas que sobrescriben el método carnivoro
class Cocodrilo(AnimalCarnivoro):
    def carnivoro(self):
        print("El cocodrilo come carne")

class Gato(AnimalCarnivoro):
    def carnivoro(self):
        print("El gato come carne")

class Tiburon(AnimalCarnivoro):
    def carnivoro(self):
        print("El tiburón come carne")

class Caiman(AnimalCarnivoro):
    def carnivoro(self):
        print("El caimán come carne")

# Función que aplica polimorfismo
def come_carne(animal):
    animal.carnivoro()

# Crear instancias
mi_cocodrilo = Cocodrilo()
mi_gato = Gato()
mi_tiburon = Tiburon()
mi_caiman = Caiman()

# Usar la función polimórfica
come_carne(mi_cocodrilo)
come_carne(mi_gato)
come_carne(mi_tiburon)
come_carne(mi_caiman)