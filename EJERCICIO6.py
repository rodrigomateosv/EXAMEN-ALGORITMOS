import random

class ArtefactoValioso:
    def __init__(self, peso, nombre, precio, fecha_caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_caducidad = fecha_caducidad
        print(f"El artefacto {self.nombre} ha sido creado con éxito.")

    def __str__(self):
        return f"Nombre: {self.nombre}, Peso: {self.peso}, Precio: {self.precio}, Fecha de caducidad: {self.fecha_caducidad}"


def llenar_mochila(precios, pesos, peso_maximo):
    dp = [[0 for _ in range(peso_maximo+1)] for _ in range(len(precios)+1)]

    for i in range(1, len(precios)+1):
        for peso in range(1, peso_maximo+1):
            if pesos[i-1] <= peso:
                dp[i][peso] = max(dp[i-1][peso], precios[i-1] + dp[i-1][peso - pesos[i-1]])
            else:
                dp[i][peso] = dp[i-1][peso]

    return dp[-1][-1]


if __name__ == "__main__":
    precios = [random.randint(10, 200) for _ in range(50)]
    pesos = [random.randint(1, 50) for _ in range(50)]
    peso_maximo = 100

    valor_maximo = llenar_mochila(precios, pesos, peso_maximo)
    print("Valor máximo que se puede obtener: ", valor_maximo)
