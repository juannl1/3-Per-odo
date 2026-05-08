import numpy as np

a = np.arange(1, 11, 2, dtype=int)
lista = list(range(1, 10, 2))

convencional = 5 * lista
numpy = 5 * a

#print(convencional)
#print(numpy)

matriz = np.ones((3, 3))
matriz[0,0] = 1
matriz[0,1] = 2
matriz[0,2] = 3
matriz[1,0] = 4
matriz[1,1] = 5
matriz[1,2] = 6
matriz[2,0] = 7
matriz[2,1] = 8
matriz[2,2] = 9






print(matriz)
