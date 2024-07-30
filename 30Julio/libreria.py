#definicion de clases
class Vehiculo():
    def __init__(self, name,color,ruedas):
        self.name = name
        self.color = color  
        self.ruedas = ruedas
    def __str__(self) -> str:
         return "Color {}, cantidad Ruedas {} Tipo de Vehiculo {}".format(self.color, self.ruedas, self.name)   

class Sedan(Vehiculo):
    def __init__(self, name, color, ruedas, motor, puertas):
        super().__init__(name, color, ruedas,)
        self.motor = motor
        self.puertas = puertas
    def __str__(self) -> str:
        return super().__str__() + "  Motor " + str(self.motor) + "  Cantidad de Puertas " + str(self.puertas)   

#fin definicio de clases
