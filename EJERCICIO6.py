def mochila(precio, peso, peso_maximo):
    n = len(precio)
    K = [[0 for w in range(peso_maximo + 1)] for i in range(n + 1)]
    
    for i in range(n + 1):
        for w in range(peso_maximo + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif peso[i-1] <= w:
                K[i][w] = max(precio[i-1] + K[i-1][w-peso[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    
    return K[n][peso_maximo]


precio = [103, 60, 70, 5, 15]
peso = [12, 23, 11, 15, 7]
peso_maximo = 100
print(mochila(precio, peso, peso_maximo))  # Output: 238

import random

# Crear una lista más grande de objetos
precios = [random.randint(10, 200) for _ in range(50)]
pesos = [random.randint(1, 50) for _ in range(50)]
peso_maximo = 100

# Crear una matriz para almacenar los resultados de subproblemas
dp = [[0 for _ in range(peso_maximo+1)] for _ in range(len(precios)+1)]

for i in range(1, len(precios)+1):
    for peso in range(1, peso_maximo+1):
        if pesos[i-1] <= peso:
            # Si el objeto cabe en la mochila, decidir si es beneficioso incluirlo o no
            dp[i][peso] = max(dp[i-1][peso], precios[i-1] + dp[i-1][peso - pesos[i-1]])
        else:
            # Si el objeto no cabe en la mochila, pasar al siguiente
            dp[i][peso] = dp[i-1][peso]

# El valor máximo se encuentra en la esquina inferior derecha de la matriz
valor_maximo = dp[-1][-1]

print("Valor máximo que se puede obtener: ", valor_maximo, "peso maximo", peso_maximo)
