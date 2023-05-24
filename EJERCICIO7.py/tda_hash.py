


from tda_lista import Lista, insertar, eliminar, busqueda, tamanio, barrido

def crear_tabla(tamanio):
    tabla = [None] * tamanio
    return tabla

def agregar_ta(tabla, hash, dato, criterio=None):
    posicion = hash(dato, tabla)
    if(tabla[posicion] is None):
        tabla[posicion] = Lista()
    insertar(tabla[posicion], dato, criterio)

def quitar_ta(tabla, hash, dato, criterio=None):
    posicion = hash(dato, tabla)
    if(tabla[posicion] is not None):
        return eliminar(tabla[posicion], dato.code, criterio)  # Modificado de dato.palabra a dato.code

def buscar_ta(tabla, hash, dato, criterio=None):
    posicion = hash(dato, tabla)
    if(tabla[posicion] is not None):
        return busqueda(tabla[posicion], dato.code, criterio)  # Modificado de dato.palabra a dato.code

def hash_division(clave, tabla):
    return clave % len(tabla)

def hash_division_troopers(trooper, tabla):
    return trooper.code % len(tabla)

def bernstein(cadena, tabla):
    """Función hash de Bernstein para cadenas."""
    h = 0
    for caracter in cadena:
        h = h * 33 + ord(caracter)
    return h % len(tabla)

def bernstein_troopers(trooper, tabla):
    """Función hash de Bernstein para cadenas."""
    h = 0
    for caracter in trooper.legion:
        h = h * 33 + ord(caracter)
    return h % len(tabla)

def cantidad_elementos_ta(tabla):
    cantidad = 0
    for elemento in tabla:
        if(elemento is not None):
            cantidad += tamanio(elemento)
    return cantidad

def cantidad_elementos_tc(tabla):
    return len(tabla) - tabla.count(None)



