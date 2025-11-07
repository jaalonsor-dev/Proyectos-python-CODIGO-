# Definamos la clase base de los Pokémons
class Pokemon:
    def __init__(self, nombre, tipo, nivel, vida, ataque, velocidad):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.vida = vida
        self.ataque = ataque
        self.velocidad = velocidad

    def descripcion(self):
   
        return f"{self.nombre} es un Pokémon de tipo {self.tipo}, nivel {self.nivel}.\n" \
               f"Vida: {self.vida}|Ataque: {self.ataque}|Velocidad: {self.velocidad}"

# Subclases específicas de Pokémons de mi equipo (Equipo de Alejandro Alonso)
class Jolteon(Pokemon):
    def __init__(self, nivel):
   
        super().__init__("Jolteon", "Eléctrico", nivel, vida=100 + nivel * 2, ataque=85 + nivel, velocidad=100)

class Charizard(Pokemon):
    def __init__(self, nivel):
        
        super().__init__("Charizard", "Fuego-Volador", nivel, vida=80 + nivel * 2, ataque=110 + nivel, velocidad=88)

class Bulbasaur(Pokemon):
    def __init__(self, nivel):
        
        super().__init__("Bulbasaur", "Planta-Veneno", nivel, vida=85 + nivel * 2, ataque=87 + nivel, velocidad=77)

class Blastoide(Pokemon):
    def __init__(self, nivel):
        
        super().__init__("Blastoide", "Agua", nivel, vida=90 + nivel * 2, ataque=87 + nivel, velocidad=77)

class Tiranitar(Pokemon):
    def __init__(self, nivel):
        
        super().__init__("Tiranitar", "Roca-Siniestro", nivel, vida=100 + nivel * 2, ataque=110 + nivel, velocidad=77)


jolteon_instance = Jolteon(nivel=65)
charizard_instance = Charizard(nivel=63) 
bulbasaur_instance = Bulbasaur(nivel=66)
blastoide_instance = Blastoide(nivel=62)
tiranitar_instance = Tiranitar(nivel=64)

# Mostrar descripciones de los pokemons de mi equipo jajajajaja
print(jolteon_instance.descripcion())
print(charizard_instance.descripcion()) 
print(bulbasaur_instance.descripcion())
print(blastoide_instance.descripcion())
print(tiranitar_instance.descripcion())