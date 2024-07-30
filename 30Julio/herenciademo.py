from  libreria import *

mNombre = input("Ingrese el nombre del vehiculo")
mColor = input("Ingrese el color del Vehiculo")
mRuedas = int(input("Ingrese la cantidad de ruedas"))
if mRuedas == 2:
    mTipo = input("Ingrese el tipo de Motocileta")
    mCilindrada = int(input("Ingrese la cilindrada"))
if mRuedas == 4:
    mMotor = input("Ingrese el Motor del Sedan")
    mPuertas = int(input("Ingrese las puertas del Sedan"))
    miSedan = Sedan(mNombre,mColor,mRuedas,mMotor,mPuertas)
    print(miSedan)

#inicio de codigo base

miCarro = Vehiculo("Carro","Rojo",2)

print(miCarro)


miSedan = Sedan("Carro","Rojo",4,1600,4)
print(miSedan)

#finde codigo principal