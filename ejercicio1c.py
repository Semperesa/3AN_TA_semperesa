import random

nums = []
for x in range(0,5):
    r = random.randint(0, 1000)
    nums.append(r)
    print(r)

is_in_list = False
while(is_in_list == False):
    print("Escribe un número")
    user = int(input())
    showmsg = True
    for x in nums:
        if user == x:
            showmsg = False
            is_in_list = True
    if showmsg == True:
        print("Ese número no está en la lista, vuelve a intentarlo...\n")
else:
    print("El número está en la lista\nFelicidades, has ganado!")
