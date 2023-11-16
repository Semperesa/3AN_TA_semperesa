import random

media = 0
lista = []

for x in range(0, 10):
    r = random.randint(0, 100)
    lista.append(r)
    media += r
print(lista)
print(media / 10)
