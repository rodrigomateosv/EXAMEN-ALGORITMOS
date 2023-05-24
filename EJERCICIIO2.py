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
    print()

import unittest
import sys



import unittest
import sys
import io


class TestStormtrooper(unittest.TestCase):
    def test_calificacion(self):
        st1 = Stormtrooper("FN-2187", "Soldado")

        original_stdout = sys.stdout  # Guarda la salida stdout original
        sys.stdout = buffer = io.StringIO()  # Redirecciona la salida stdout a buffer

        st1.calificacion()

        sys.stdout = original_stdout  # Restaura la salida stdout original
        salida = buffer.getvalue()  # Extrae la cadena de la salida capturada
        
        self.assertEqual(salida.strip(), "FN-2187 es un miembro común de las tropas del Imperio Galáctico.")

        # Aquí puedes agregar los otros casos de prueba

if __name__ == '__main__':
    unittest.main()
