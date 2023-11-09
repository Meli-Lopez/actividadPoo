class Persona:
    # Atributos de la clase
    nombre = ""
    apellido = ""
    edad = 0

    # Metodo para inicializar la clase (constructor)
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Metodo para mostrar informacion de la persona
    def mostrarInformacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")

# Crear una instancia de la clase Persona
persona1 = Persona("Neylliber", "Melissa", 16)

# Llama el metodo para mostrar los datos de la persona
persona1.mostrarInformacion()