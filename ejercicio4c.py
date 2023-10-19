# c) Basándose en el apartado anterior, complete esta jerarquía
# rellenando los nuevos métodos a su criterio
# Clase Vehículo:
#     Atributos: gasolina
#     Métodos: Inicializar, PonerGasolina, ConsumirGasolina
#
# Clase Moto : Vehículo:
#     Atributos: gasolina, pasajero
#     Métodos: Inicializar, PonerGasolina, ConsumirGasolina, SubirPasajero, BajarPasajero
#
# Clase Coche : Vehículo:
#     Atributos: gasolina, puertas, abiertas
#     Métodos: Inicializar, PonerGasolina, ConsumirGasolina, AbrirPuertas, CerrarPuertas

class Vehiculo:
    def __init__(self, gasolina):
        self.gasolina = gasolina

    def ponergasolina(self, gasolina):
        self.gasolina += gasolina

    def consumirgasolina(self, gasolina):
        self.gasolina -= gasolina

class Moto(Vehiculo):
    def __init__(self, gasolina, pasajero):
        super().__init__(gasolina)
        self.pasajero = pasajero

    def subirpasajero(self):
        self.pasajero = True

    def bajarpasajero(self):
        self.pasajero = False

    def __str__(self):
        return f"Vehículo: Moto, Gasolina: {self.gasolina}, Pasajero: {self.pasajero}"

class Coche(Vehiculo):
    def __init__(self, gasolina, puertas, abiertas):
        super().__init__(gasolina)
        self.puertas = puertas
        self.abiertas = abiertas

    def abrirpuertas(self):
        self.abiertas = True

    def cerrarpuertas(self):
        self.abiertas = False

    def __str__(self):
        return f"Vehículo: Coche, Gasolina: {self.gasolina}, Puertas: {self.puertas}, Abiertas: {self.abiertas}"

m = Moto(50, True)
print(m)
m.ponergasolina(10)
print("Poner gasolina:\n\t", m)
m.consumirgasolina(25)
print("Consumir gasolin:\n\t", m)
m.bajarpasajero()
print("Bajar pasajero:\n\t", m)
m.subirpasajero()
print("Subir pasajero:\n\t:", m, "\n\n")

c = Coche(75, 4, False)
print(c)
c.ponergasolina(10)
print("Poner gasolina\n\t", c)
c.consumirgasolina(40)
print("Consumir gasolina\n\t", c)
c.abrirpuertas()
print("Abrir puertas:\n\t", c)
c.cerrarpuertas()
print("Cerrar puertas:\n\t", c)


