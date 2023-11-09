# Se crea la clase
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}.")

# Clase derivada (hereda de Persona)
class datos(Persona):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido)
        self.edad = edad 

    def dato(self):
        print(f"Mi edad es {self.edad}. ")

# Crear una instancia de la clase Estudiante
estudiante1 = datos("Neylliber", "Lopez", 16)

# Acceder a los atributos y metodos de la clase saludar y la clase base Persona
print(estudiante1.nombre)  # Muestra el nombre
print(estudiante1.apellido) # Muestra el apellido
print(estudiante1.edad)  # Muestra la edad
estudiante1.saludar()
estudiante1.dato()