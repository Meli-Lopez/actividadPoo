# Se crea la clase
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} {self.apellido}.")

# Clase derivada
class aprendiz(Persona):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido)
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} {self.apellido} y tengo {self.edad} años.")

# Crear una instancia de la clase Persona
persona1 = Persona("Neylliber", "Lopez")
persona1.saludar()

# Crear una instancia de la clase aprendiz
aprendiz1 = aprendiz("Melissa", "Higinio", 16)
aprendiz1.saludar()
