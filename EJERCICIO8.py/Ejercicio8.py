from tda_heap2 import Heap, agregar, quitar, cantidad_elementos

from tda_heap2 import Heap, agregar, quitar, cantidad_elementos

class Nodo:
    def __init__(self, char, freq):
        self.nodo = [freq, char]
        self.izq = None
        self.der = None

    def __getitem__(self, index):
        return self.nodo[index]

    def __setitem__(self, index, val):
        self.nodo[index] = val

    @property
    def char(self):
        return self.nodo[1]

    @property
    def freq(self):
        return self.nodo[0]

# El resto del código sigue aquí sin cambios...


def fusionar_nodos(heap):
    while(cantidad_elementos(heap)>1):
        nodo1 = quitar(heap)
        nodo2 = quitar(heap)

        fusionado = Nodo(None, nodo1.freq + nodo2.freq)
        fusionado.izq = nodo1
        fusionado.der = nodo2

        agregar(heap, fusionado)

def codificar_aux(root, actual_codigo, codigos, invertir_codigos):
    if root is None:
        return

    if root.char is not None:
        codigos[root.char] = actual_codigo
        invertir_codigos[actual_codigo] = root.char
        return

    codificar_aux(root.izq, actual_codigo + "0", codigos, invertir_codigos)
    codificar_aux(root.der, actual_codigo + "1", codigos, invertir_codigos)

def codificar(heap):
    root = quitar(heap)
    codigos = {}
    invertir_codigos = {}
    codificar_aux(root, "", codigos, invertir_codigos)
    return codigos, invertir_codigos

def comprimir(texto, codigos):
    res = ""
    for character in texto:
        res += codigos[character]
    return res

def descomprimir(texto_comprimido, invertir_codigos):
    codigo_actual = ""
    res = ""

    for bit in texto_comprimido:
        codigo_actual += bit
        if codigo_actual in invertir_codigos:
            character = invertir_codigos[codigo_actual]
            res += character
            codigo_actual = ""

    return res

frecuencia = {'A': 0.2, 'F': 0.17, '1': 0.13, '3': 0.21, '0': 0.05, 'M': 0.09, 'T': 0.15}
heap = Heap(len(frecuencia))

for key in frecuencia:
    nodo = Nodo(key, frecuencia[key])
    agregar(heap, nodo)

fusionar_nodos(heap)
codigos, invertir_codigos = codificar(heap)

texto = 'AFA31130MTM'
texto_comprimido = comprimir(texto, codigos)
print('Texto comprimido:', texto_comprimido)

texto_descomprimido = descomprimir(texto_comprimido, invertir_codigos)
print('Texto descomprimido:', texto_descomprimido)
