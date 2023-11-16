# a) Una persona tiene nombre, dos apellidos y DNI. A esa persona se le
# puede cambiar el nombre y se le pueden invertir los apellidos, pero no
# se le puede cambiar el DNI nunca. Un futbolista también es una
# persona, pero además juega en un equipo concreto, en una posición en
# concreto y cobra un sueldo en euros. Se le puede cambiar de equipo y
# de posición, y su sueldo sólo varía en incrementos de 1 millón.

class Persona:
    def __init__(self, nombre, apellido1, apellido2, dni):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.__dni = dni

    def cambiarnombre(self, nuevonombre):
        self.nombre = nuevonombre

    def invertirapellidos(self):
        tmp = self.apellido1
        self.apellido1 = self.apellido2
        self.apellido2 = tmp

    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido1} {self.apellido2}, DNI: {self.__dni}"

class Futbolista(Persona):
    def __init__(self, nombre, apellido1, apellido2, dni, equipo, posicion, sueldo):
        super().__init__(nombre, apellido1, apellido2, dni)
        self.equipo = equipo
        self.posicion = posicion
        self.sueldo = sueldo

    def cambiarequipo(self, nuevoequipo):
        self.equipo = nuevoequipo

    def cambiarposicion(self, nuevaposicion):
        self.posicion = nuevaposicion

    def subirsueldo(self, cantidad):
        self.sueldo += cantidad * 1000000

    def bajarsueldo(self, cantidad):
        self.sueldo -= cantidad * 1000000

    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido1} {self.apellido2}, Equipo: {self.equipo}, Posición: {self.posicion}, Sueldo: {self.sueldo}"

print("--- PERSONA ---")
p = Persona("Peter", "Ben", "Parker", "123456789S")
print("Persona:\n\t", p)
p.cambiarnombre("Harry")
print("Cambio de nombre:\n\t", p)
p.invertirapellidos()
print("Invertir apellidos\n\t:", p)
p.__dni = "jajaja"
print("Intentar cambiar DNI:\n\t", p)

print("--- FUTBOLISTA ---")
f = Futbolista("Pedro", "Picapiedra", "Rocadura", "444555666J", "MartillosFC", "Defensa", 3000000)
print("Futbolista:\n\t", f)
f.cambiarnombre("Pablo")
print("Cambio de nombre:\n\t", f)
f.invertirapellidos()
print("Apellidos invertidos\n\t", f)
f.cambiarequipo("ChispasFC")
print("Cambio de equipo\n\t", f)
f.cambiarposicion("Delantero")
print("Cambio de posición:\n\t", f)
f.subirsueldo(10)
print("Aumento de sueldo:\n\t", f)
f.bajarsueldo(5)
print("Reduccion de sueldo:\n\t", f)

    
