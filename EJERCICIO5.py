class ArtefactoValioso:
    def __init__(self, peso, nombre, precio, fecha_caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_caducidad = fecha_caducidad
        print(f'El artefacto {self.nombre} ha sido creado con éxito.')

    def __str__(self):
        return f'Nombre: {self.nombre}, Peso: {self.peso}, Precio: {self.precio}, Fecha de Caducidad: {self.fecha_caducidad}'


def usar_la_fuerza(mochila, cuenta=0):
    if len(mochila) == 0:
        return False, cuenta
    elif mochila[0] == 'sable de luz':
        return True, cuenta + 1
    else:
        return usar_la_fuerza(mochila[1:], cuenta + 1)


# Crear algunos artefactos valiosos
artefacto1 = ArtefactoValioso(10, 'Artefacto 1', 1000, '2023-12-31')
artefacto2 = ArtefactoValioso(5, 'Artefacto 2', 500, '2023-06-01')
artefacto3 = ArtefactoValioso(15, 'Artefacto 3', 1500, '2024-01-01')

# Modificar el precio de un artefacto
artefacto1.precio = 1100

# Mostrar los datos de los artefactos
print(artefacto1)
print(artefacto2)
print(artefacto3)

# Probar la función usar_la_fuerza
mochila = ['manzana', 'agua', 'sable de luz', 'manta', 'libro']
encontrado, objetos_sacados = usar_la_fuerza(mochila)
if encontrado:
    print(f'Se encontró el sable de luz después de sacar {objetos_sacados} objetos.')
else:
    print(f'No se encontró el sable de luz. Se sacaron {objetos_sacados} objetos.')
