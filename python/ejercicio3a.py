# a) Contenga una función que reciba dos listas como parámetros.
# Primero ha de comprobar si ambas listas tienen la misma longitud, y en
# caso afirmativo, la función ha de devolver un diccionario usando como
# claves los elementos de la primera lista y como valores los de la
# segunda

def func(lista, listb):
    if (len(lista) == len(listb)):
        d = {}
        for x in range(0, len(lista)):
            d[lista[x]] = listb[x] 
        print(d)
    else:
        print("Las listas no tienen el mismo número de elementos")

lista = ['a','b','c']
listb = [1,2,3]
func(lista, listb)

lista = ['a']
listb = [1,2]
func(lista, listb)

