persona = []

print("Escribe tu nombre: ")
nombre = input()
persona.insert(0, nombre)
print("Tu nombre es " + nombre + "\n")

print("Escribe tu teléfono: ")
tlf = input()
persona.insert(0, tlf)
print("Tu teléfono es " + tlf + "\n")

print("Escribe tu direccion: ")
direccion = input()
persona.insert(0, direccion)
print("Tu dirección es " + direccion + "\n")

print("Estos son tus datos: ", persona)
