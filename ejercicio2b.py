# b) Que dada una lista con los 10 primeros
# números naturales (función range() ), cree otra lista vacía
# y copie sólo los números pares de la primera lista en ella

lista = []
for x in range(1, 11):
    lista.append(x)
listb = []
print(lista)
for x in lista:
    if x % 2 == 0:
        listb.append(x)
print(listb)
