#Defiendo las clases
class ClasePadre:
    def __init__(self,) -> None:
        self.Nombre = input("Ingrese un nombre de usuario ")
        self.Edad = int(input("Cual es su Edad"))
        self.Salario = int(input("Cual es su salario "))
        self.Descuentos = int(input("Ingrese descuentos"))
class claseHija(ClasePadre):
    def __init__(self) -> None:
        super().__init__()



#fin de definicion de las clases




#programa principal

miObjeto = ClasePadre()
print(f"Su nombre es {miObjeto.Nombre} su edad es {miObjeto.Edad} su salario base es de {miObjeto.Salario}")


miObjeto2 = claseHija()
print(f"Su nombre es {miObjeto2.Nombre} su edad es {miObjeto2.Edad} su salario base es de {miObjeto2.Salario}")


#fin de programa principal