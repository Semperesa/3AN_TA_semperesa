# b) Crear la clase coche con la siguiente estructura
# Clase Coche:
#     exporta: Inicializar, PonerGasolina, ConsumirGasolina, AbrirPuertas, CerrarPuertas;
#     attributos: entero puertas, booleano abiertas, real gasolina
#     métodos:
#         Inicializar( entero g, entero p) { puertas = p, gasolina = g, abiertas = CIERTO }
#         PonerGasolina ( entero g ) { gasolina = gasolina + g }
#         ConsumirGasolina ( entero g ) { gasolina = gasolina - g }
#         AbrirPuertas () { abiertas = CIERTO }
#         CerrarPuertas () { abiertas = FALSO }

class Coche:
    def __init__(self, gasolina, puertas):
        self.gasolina = gasolina
        self.puertas = puertas
        self.abiertas = True        

    def ponergasolina(self, gasolina):
        self.gasolina += gasolina

    def consumirgasolina(self, gasolina):
        self.gasolina -= gasolina

    def abrirpuertas(self):
        self.abiertas = True

    def cerrarpuertas(self):
        self.abiertas = False

    def __str__(self):
        return f"Gasolina: {self.gasolina}, Puertas: {self.puertas}, Abiertas: {self.abiertas}"

c = Coche(100, 4)
print("Coche:\n\t", c)
c.ponergasolina(20)
print("Poner gasolina:\n\t", c)
c.consumirgasolina(50)
print("Consumir gasolina:\n\t", c)
c.cerrarpuertas()
print("Cerrar puertas:\n\t", c)
c.abrirpuertas()
print("Abrir puertas:\n\t", c)




