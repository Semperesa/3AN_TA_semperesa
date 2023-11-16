# b) Contenga dos funciones: una para pasar a minúsculas todos los
# elementos de tipo cadena de una lista y otra para pasarlos a
# mayúsculas

def minus (lista):
    for x in range(len(lista)):        
        if type(lista[x]) is str:
            lista[x] = lista[x].lower()

def mayus (lista):
    for x in range(len(lista)):
        if type(lista[x]) is str:
            lista[x] = lista[x].upper()

lista = ['Hola', 1, True, 'Mundo']
print(lista)

minus(lista)
print(lista)

mayus(lista)
print(lista)
