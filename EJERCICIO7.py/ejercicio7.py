import random
from tda_lista import Lista, insertar, eliminar, busqueda, barrido
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
