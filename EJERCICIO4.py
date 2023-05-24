from datetime import datetime

class ArtefactosValiosos:
    def __init__(self, peso, nombre, precio, fecha_caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_caducidad = datetime.strptime(fecha_caducidad, '%Y-%m-%d')
        print(f'El artefacto valioso {self.nombre} se ha creado con éxito.')

    def __str__(self):
        return f'Nombre: {self.nombre}, Peso: {self.peso}kg, Precio: {self.precio}$, Fecha de caducidad: {self.fecha_caducidad.strftime("%Y-%m-%d")}'


# Crear artefactos valiosos
artefactos = [
    ArtefactosValiosos(2.5, 'Esmeralda Mística', 5000, '2024-12-31'),
    ArtefactosValiosos(1.2, 'Rubí Encantado', 3500, '2023-11-01'),
    ArtefactosValiosos(3.0, 'Diamante Eterno', 8000, '2025-01-01'),
    ArtefactosValiosos(0.5, 'Perla de la Sabiduría', 2000, '2023-06-15'),
]

# Ordenar por fecha de caducidad
artefactos.sort(key=lambda x: x.fecha_caducidad)

# Imprimir artefactos
for artefacto in artefactos:
    print(artefacto)

# Cambiar el precio de un artefacto
artefactos[0].precio = 6000
print(f'\nDespués de cambiar el precio:\n{artefactos[0]}')
