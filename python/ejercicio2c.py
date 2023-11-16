#c) Que dada una cadena, cree una lista con
# cada una de las letras de la cadena como elementos

print("Escribe una cadena de texto")
cadena = input()
print("Tu cadena de texcto ", cadena)
lista = []
for letra in cadena:
    lista.append(letra)
print("Lista de cáracteres")
print(lista)
