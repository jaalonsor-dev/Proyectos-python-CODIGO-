#cLASE PARA MOSTRAR LOS DATOS DE UN PACIENTE

class Paciente:
  def __init__(self, nombre, edad, sexo, peso, altura):
    self.nombre = "Andres Felipe Alonso Rondon"
    self.edad = "15"
    self.sexo = "Masculino"
    self.peso = "57"
    self.altura = "176 Cm"

Paciete = Paciente("Andres Felipe Alonso Rondon", "15", "Masculino", "57", "176 Cm")
print(Paciete.nombre)
print(Paciete.edad)
print(Paciete.sexo)
print(Paciete.peso)
print(Paciete.altura)