#Clase Definicion
class Empleado :
        def __init__(self) -> None:
                self.Nombre = input("Ingrese su nombre ")
                self.Salario = float(input("Ingrese su salario "))
                self.OtrosIngresos = float(input("Ingrese Otros Ingresos "))
                self.Descuentos = float(input("Ingrese Otros Descuentos  "))
        
        def CalcularSalario(self):
                return float(self.Salario) + float(self.OtrosIngresos) - float(self.Descuentos)
 #termina definicion de la clase
 # 

#Definir la clase hija Administrativo 
class Administrativo(Empleado):
        def __init__(self) -> None:
                super().__init__()
                self.Bono = float (input("Ingrese el bono del vendedor $"))
        def CalcularLiquidoAdministrador():
            return super().CalcularSalario 
#fin de la definicion de la clase hija admisnitrativo

 # inicia el bloque principal del programa             
miAdmin = Administrativo()

print(miAdmin.CalcularSalario())


