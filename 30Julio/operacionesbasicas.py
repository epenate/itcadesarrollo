class Operaciones:
    def __init__(self, *args,) -> None: 
        self.Operando1=float(input("Ingrese el primer valor"))
        self.Operando2=float(input("Ingrese el segundo valor"))
    
    def Suma(self) -> float:
        return self.Operando1 + self.Operando2
    def Resta(self) -> float:
        return self.Operando1 - self.Operando2
    def Multiplica (self) -> float:
        return self.Operando1 * self.Operando2
    def Divide (self) -> float:
        return self.Operando1 / self.Operando2


#bloque principal del programa
miCalculadoraBasica = Operaciones()

print (f"La suma es {miCalculadoraBasica.Suma()}")
