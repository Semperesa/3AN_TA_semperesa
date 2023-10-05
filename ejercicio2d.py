#d) Que pida que el usuario introduzca una frase en inglés o castellano
#sin tildes y la almacene. Después el programa debe devolver una lista
#de 5 elementos (uno para cada vocal) con el número de apariciones de
#cada vocal en la frase. E.g:
#“One ring to rule them all” ==> [1, 3, 1, 2, 1]
#“Esta frase contiene unas cuantas letras” ==> [6, 5, 1, 1, 2]

print("Escribe una cadena de texto")
cadena = input()
vocales = [0, 0, 0, 0, 0]
for vocal in cadena:
    if(vocal == "A" or vocal == "a"):
        vocales[0] += 1
    if(vocal == "E" or vocal == "e"):
        vocales[1] += 1
    if(vocal == "I" or vocal == "i"):
        vocales[2] += 1
    if(vocal == "O" or vocal == "o"):
        vocales[3] += 1
    if(vocal == "U" or vocal == "u"):
        vocales[4] += 1

print(vocales)
