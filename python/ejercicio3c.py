# c) Contega una función que, dado un diccionario, devuelva otro con
# aquellos elementos cuya clave sea una cadena de menos de 5
# caracteres

def func(dic):
    print(dic)
    d = {}
    for clave, valor in dic.items():
        if type(clave) is str and len(clave) < 5:
            d[clave] = valor;
    print(d)

d = { "Hola" : 1, "Quetal" : "Pepe", "Jaja" : True, 2 : "Sí" }

func(d)
