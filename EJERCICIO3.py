class Stormtrooper:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print("El Stormtrooper", self.nombre, "ha sido creado con éxito.")

    def calificacion(self):
        if self.rango == "General":
            print(self.nombre, "es un alto mando en el Imperio Galáctico.")
        elif self.rango == "Capitán":
            print(self.nombre, "lidera a un grupo de Stormtroopers.")
        elif self.rango == "Soldado":
            print(self.nombre, "es un miembro común de las tropas del Imperio Galáctico.")
        else:
            print("Rango desconocido para el Stormtrooper", self.nombre)
            
    def __str__(self):
        return "Stormtrooper: Nombre: " + self.nombre + ", Rango: " + self.rango


# Crear una lista de stormtroopers
stormtroopers = [
    Stormtrooper("FN-2187", "Soldado"),
    Stormtrooper("CT-7567", "Capitán"),
    Stormtrooper("CC-1010", "General"),
    Stormtrooper("TK-421", "Ingeniero"),
    Stormtrooper("DS-61-2", "Piloto")
]

# Recorrer la lista y ejecutar el método de calificación
for stormtrooper in stormtroopers:
    stormtrooper.calificacion()
    
# Imprimir la información de cada stormtrooper utilizando __str__
for stormtrooper in stormtroopers:
    print(stormtrooper)
