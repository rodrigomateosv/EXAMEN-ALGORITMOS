import random
from tda_lista import Lista, insertar, eliminar, busqueda, barrido, get_elements
from tda_hash import crear_tabla, agregar_ta, quitar_ta, buscar_ta, hash_division, bernstein

class Stormtrooper:
    def __init__(self, legion, code):
        self.legion = legion
        self.code = code

    def __str__(self):
        return f'{self.legion}-{self.code}'

# Generar 2000 Stormtroopers
legions = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']
stormtroopers = [Stormtrooper(random.choice(legions), str(random.randint(1000,9999))) for _ in range(2000)]

# Crear tablas hash
tabla1 = crear_tabla(1000)
tabla2 = crear_tabla(26)

# Funciones hash personalizadas
def hash_last_three(stormtrooper, tabla):
    return int(stormtrooper.code[-3:]) % len(tabla)

def hash_legion(stormtrooper, tabla):
    return ord(stormtrooper.legion[0].upper()) % len(tabla)

def comparar_stormtroopers(st1, st2):
    return int(st1.code) - int(st2.code)


# Cargar Stormtroopers en las tablas hash
for stormtrooper in stormtroopers:
    agregar_ta(tabla1, hash_last_three, stormtrooper)
    agregar_ta(tabla2, hash_legion, stormtrooper)
    agregar_ta(tabla2, hash_legion, stormtrooper, comparar_stormtroopers)


# Buscar y eliminar FN-2187
fn_2187 = Stormtrooper('FN', '2187')

# Buscar en la primera tabla
pos = buscar_ta(tabla1, hash_last_three, fn_2187)
if pos is not None:
    print('FN-2187 encontrado en la primera tabla. Procediendo a eliminar.')
    quitar_ta(tabla1, hash_last_three, fn_2187)

# Buscar en la segunda tabla
pos = buscar_ta(tabla2, hash_legion, fn_2187)
if pos is not None:
    print('FN-2187 encontrado en la segunda tabla. Procediendo a eliminar.')
    quitar_ta(tabla2, hash_legion, fn_2187)

# Misión de asalto: Stormtroopers terminados en 781
print("\nMisión de asalto: Stormtroopers terminados en 781")
for i in range(len(tabla1)):
    for stormtrooper in get_elements(tabla1[i]):
        if stormtrooper.code.endswith('781'):
            print(stormtrooper)

# Misión de exploración: Stormtroopers terminados en 537
print("\nMisión de exploración: Stormtroopers terminados en 537")
for i in range(len(tabla1)):
    for stormtrooper in get_elements(tabla1[i]):
        if stormtrooper.code.endswith('537'):
            print(stormtrooper)

# Misión de custodia a Darth Vader: Stormtroopers de la legión CT
print("\nMisión de custodia a Darth Vader: Stormtroopers de la legión CT")
for i in range(len(tabla2)):
    for stormtrooper in get_elements(tabla2[i]):
        if stormtrooper.legion == 'CT':
            print(stormtrooper)

# Misión de exterminación a Endor: Stormtroopers de la legión TF
print("\nMisión de exterminación a Endor: Stormtroopers de la legión TF")
for i in range(len(tabla2)):
    for stormtrooper in get_elements(tabla2[i]):
        if stormtrooper.legion == 'TF':
            print(stormtrooper)


