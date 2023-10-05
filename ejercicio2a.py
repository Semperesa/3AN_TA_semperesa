#a) Cree una lista vacía, pida por teclado 10 números y
# luego saque la media, el máximo y el mínimo de todos ellos

lista = []
maxnum = 10
media = 0
for x in range(0,maxnum):
    print("inserta un numero")
    num = int(input())
    lista.append(num)
    media += num
media /= maxnum;
lista.sort()
print("La media es ", media)
print("El número mínimo es ", lista[0])
print("El número máximo es ", lista[-1])

