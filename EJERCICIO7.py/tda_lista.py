class nodoLista(object):

    def __init__(self):
        self.info = None
        self.sig = None


class Lista(object):

    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def insertar(lista, dato, campo=None):
    nodo = nodoLista()
    nodo.info = dato
    if(lista.inicio is None or lista.inicio.info.code > nodo.info.code):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        act = lista.inicio.sig
        ant = lista.inicio
        while(act is not None and act.info.code < nodo.info.code):
            act = act.sig
            ant = ant.sig

        nodo.sig = act
        ant.sig = nodo

    lista.tamanio += 1    


def eliminar(lista, clave, campo=None):
    dato = None
    if(lista.inicio.info.code == clave):
        dato = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamanio -= 1
    else:
        act = lista.inicio.sig
        ant = lista.inicio
        while(act is not None and act.info.code != clave):
            act = act.sig
            ant = ant.sig
        
        if(act is not None):
            dato = act.info
            ant.sig = act.sig
            lista.tamanio -= 1

    return dato


def busqueda(lista, clave, campo=None):
    aux = lista.inicio
    while(aux is not None and aux.info.code != clave):
        aux = aux.sig
    return aux


def barrido(lista):
    aux = lista.inicio
    while(aux is not None):
        print(aux.info)
        aux = aux.sig

def get_elements(lista):
    """Devuelve una lista de todos los elementos en la lista."""
    elements = []
    if lista is not None:
        aux = lista.inicio
        while aux is not None:
            elements.append(aux.info)
            aux = aux.sig
    return elements

    

def tamanio(lista):
    return lista.tamanio


def lista_vacia(lista):
    return lista.inicio is None
